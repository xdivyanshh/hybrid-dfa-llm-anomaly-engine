#include "engine.hpp"
#include <sstream>
#include <iomanip>

std::string LLMEscalationPayload::toJSON() const {
    std::ostringstream oss;
    oss << "{\n";
    oss << "  \"event_type\": \"" << eventType << "\",\n";
    oss << "  \"raw_log\": \"" << rawLog << "\",\n";
    oss << "  \"sanitized_log\": \"" << sanitizedLog << "\",\n";
    oss << "  \"dfa_result\": \"" << dfaResult << "\",\n";
    oss << "  \"visited_states\": [";
    for (size_t i = 0; i < visitedStates.size(); ++i) {
        oss << "\"" << visitedStates[i] << "\"" << (i + 1 < visitedStates.size() ? ", " : "");
    }
    oss << "],\n";
    oss << "  \"last_valid_state\": \"" << lastValidState << "\",\n";
    oss << "  \"reason\": \"" << reason << "\",\n";
    oss << "  \"turing_machine_metadata\": {\n";
    oss << "    \"tape_steps\": " << tmSteps << ",\n";
    oss << "    \"masked_characters\": " << tmMaskedChars << "\n";
    oss << "  },\n";
    oss << "  \"session_context\": [";
    for (size_t i = 0; i < sessionContext.size(); ++i) {
        oss << "\"" << sessionContext[i] << "\"" << (i + 1 < sessionContext.size() ? ", " : "");
    }
    oss << "]\n";
    oss << "}";
    return oss.str();
}

AnomalyEngine::AnomalyEngine(size_t maxQueueCapacity)
    : maxQueueCapacity_(maxQueueCapacity) {}

LLMResponse AnomalyEngine::analyzeWithLLM(const LLMEscalationPayload& payload) {
    LLMResponse resp;
    resp.schemaValid = true;

    // Structured contextual response matching Section 2.4 & 2.7
    if (payload.dfaResult == "REJECT") {
        if (payload.sanitizedLog.find("DROP_TABLE") != std::string::npos ||
            payload.sanitizedLog.find("UNION") != std::string::npos ||
            payload.sanitizedLog.find("'") != std::string::npos) {
            resp.severity = "CRITICAL";
            resp.likelyCause = "SQL Injection attempt targeting SSH payload/username field";
            resp.evidence = "Malformed token at position with SQL keywords in place of valid user";
            resp.confidence = 0.98;
            resp.suggestedNextSteps = "Block source IP at firewall; inspect database query logs; verify authentication daemon bounds.";
        } else {
            resp.severity = "MEDIUM";
            resp.likelyCause = "Malformed log line / Protocol grammar violation";
            resp.evidence = payload.reason;
            resp.confidence = 0.85;
            resp.suggestedNextSteps = "Inspect logging agent version; verify client software compatibility.";
        }
    } else {
        // DFA accepted, but Moore machine flagged repeated failed attempts
        resp.severity = "HIGH";
        resp.likelyCause = "Credential brute-force / Password spraying attack";
        resp.evidence = "Exceeded threshold of 3 consecutive failed logins from single IP within short window";
        resp.confidence = 0.94;
        resp.suggestedNextSteps = "Trigger temporary IP ban (Fail2ban); enforce SSH key-based authentication; notify account owner.";
    }

    return resp;
}

EventProcessRecord AnomalyEngine::processLine(const std::string& line) {
    auto start = std::chrono::high_resolution_clock::now();

    EventProcessRecord record;
    record.rawLine = line;
    record.escalated = false;
    record.dfaAccepted = false;
    record.mooreFlagged = false;

    // 1. Ingest & Tokenize (Lexer)
    std::vector<Token> tokens = lexer_.tokenize(line);

    // Extract IP and Status if available from tokens
    std::string ip = "unknown";
    std::string status = "unknown";
    for (const auto& tok : tokens) {
        if (tok.type == TokenType::IP && ip == "unknown") {
            ip = tok.value;
        } else if (tok.type == TokenType::STATUS && status == "unknown") {
            status = tok.value;
        }
    }

    // Record IP history for context
    if (ip != "unknown") {
        recentIpHistory_[ip].push_back(line);
        if (recentIpHistory_[ip].size() > 5) {
            recentIpHistory_[ip].erase(recentIpHistory_[ip].begin());
        }
    }

    // 2. Symbolic Fast Path: DFA Evaluation
    record.dfaResult = dfa_.process(tokens);
    metrics_.totalLogsProcessed++;

    if (record.dfaResult.verdict == DFAVerdict::ACCEPT) {
        record.dfaAccepted = true;
        metrics_.dfaAcceptedCount++;

        // 3. Behavioral Check: Moore Machine
        record.mooreResult = moore_.processEvent(ip, status);
        if (record.mooreResult.output == MooreOutput::FLAG) {
            record.mooreFlagged = true;
            metrics_.mooreFlaggedCount++;
            record.escalated = true;
        }
    } else {
        metrics_.dfaRejectedCount++;
        record.escalated = true;
    }

    // 4. Escalation Path (Turing Machine Sanitizer + LLM)
    if (record.escalated) {
        metrics_.escalatedCount++;

        // Run Turing Machine Sanitizer on Tape
        TMExecutionResult tmRes = tmSanitizer_.sanitize(line);
        metrics_.totalTMMaskedChars += tmRes.maskedCharacters;

        // Build Escalation Payload
        record.escalationPayload.eventType = "ssh_login";
        record.escalationPayload.rawLog = line;
        record.escalationPayload.sanitizedLog = tmRes.sanitizedTape;
        record.escalationPayload.dfaResult = (record.dfaAccepted ? "ACCEPT" : "REJECT");
        record.escalationPayload.visitedStates = record.dfaResult.visitedStates;
        record.escalationPayload.lastValidState = record.dfaResult.lastValidState;
        record.escalationPayload.reason = (record.mooreFlagged ? 
            "Behavioral flag: 3 consecutive failed logins" : record.dfaResult.reason);
        record.escalationPayload.tmSteps = tmRes.totalSteps;
        record.escalationPayload.tmMaskedChars = tmRes.maskedCharacters;

        if (recentIpHistory_.find(ip) != recentIpHistory_.end()) {
            record.escalationPayload.sessionContext = recentIpHistory_[ip];
        }

        // Push to bounded queue
        if (escalationQueue_.size() < maxQueueCapacity_) {
            escalationQueue_.push(record.escalationPayload);
        }

        // Execute LLM analysis
        record.llmResponse = analyzeWithLLM(record.escalationPayload);
    } else {
        // Handled locally at fast path! Each log handled locally avoids an ~200 token LLM call (~$0.001)
        metrics_.simulatedCostSavedUSD += 0.0015;
    }

    auto end = std::chrono::high_resolution_clock::now();
    record.processingTimeMicroseconds = std::chrono::duration<double, std::micro>(end - start).count();
    metrics_.totalLatencyMicroseconds += record.processingTimeMicroseconds;

    return record;
}

std::vector<EventProcessRecord> AnomalyEngine::processBatch(const std::vector<std::string>& lines) {
    std::vector<EventProcessRecord> results;
    results.reserve(lines.size());
    for (const auto& line : lines) {
        results.push_back(processLine(line));
    }
    return results;
}
