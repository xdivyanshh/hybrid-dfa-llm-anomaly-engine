#include "engine.hpp"
#include <iostream>
#include <fstream>
#include <iomanip>

void printBanner() {
    std::cout << "\n================================================================================\n";
    std::cout << "       HYBRID DFA-LLM ANOMALY ENGINE WITH TURING MACHINE SANITIZER\n";
    std::cout << "  A Neuro-Symbolic Log Triage System (JIIT Dept. of CSE - Theory of Computation)\n";
    std::cout << "================================================================================\n\n";
}

void printDivider() {
    std::cout << "--------------------------------------------------------------------------------\n";
}

int main(int argc, char* argv[]) {
    printBanner();

    std::string logFilePath = "data/test_corpus.log";
    if (argc > 1) {
        logFilePath = argv[1];
    }

    std::ifstream file(logFilePath);
    if (!file.is_open()) {
        std::cerr << "[-] Error opening log file: " << logFilePath << std::endl;
        std::cerr << "[!] Retrying with absolute/fallback path..." << std::endl;
        file.open("C:/Users/Ritesh Kumar Agarwal/.gemini/antigravity/scratch/hybrid-anomaly-engine/data/test_corpus.log");
        if (!file.is_open()) {
            std::cerr << "[-] Failed to open test log file." << std::endl;
            return 1;
        }
    }

    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) {
        if (!line.empty() && line[0] != '#') {
            lines.push_back(line);
        }
    }
    file.close();

    std::cout << "[*] Loaded " << lines.size() << " log events from corpus.\n";
    std::cout << "[*] Initializing symbolic engines (DFA, Moore Machine, Turing Machine)...\n";

    AnomalyEngine engine(1000);

    for (size_t i = 0; i < lines.size(); ++i) {
        printDivider();
        std::cout << "EVENT #" << (i + 1) << ": " << lines[i] << "\n";
        
        EventProcessRecord rec = engine.processLine(lines[i]);

        std::cout << " [1] DFA VERDICT       : " 
                  << (rec.dfaAccepted ? "\033[32m[ACCEPT]\033[0m" : "\033[31m[REJECT]\033[0m")
                  << " -> Path: ";
        for (size_t s = 0; s < rec.dfaResult.visitedStates.size(); ++s) {
            std::cout << rec.dfaResult.visitedStates[s] 
                      << (s + 1 < rec.dfaResult.visitedStates.size() ? " -> " : "");
        }
        std::cout << "\n";

        if (rec.dfaAccepted) {
            std::cout << " [2] MOORE MONITOR     : State " 
                      << MooreResult::stateToString(rec.mooreResult.currentState)
                      << " (" << MooreResult::outputToString(rec.mooreResult.output) << ")"
                      << " | Failures: " << rec.mooreResult.consecutiveFailures << "\n";
        }

        if (rec.escalated) {
            std::cout << " [!] ESCALATION PATH   : Triggered -> Forwarded to Turing Machine Sanitizer\n";
            std::cout << " [3] TURING MACHINE    : Tape Sanitized (" 
                      << rec.escalationPayload.tmMaskedChars << " chars masked in " 
                      << rec.escalationPayload.tmSteps << " tape steps)\n";
            std::cout << "     Clean Tape Output : " << rec.escalationPayload.sanitizedLog << "\n";
            std::cout << " [4] NEURAL SLOW PATH  : Structured LLM Assessment Generated\n";
            std::cout << "     Severity          : " << rec.llmResponse.severity << "\n";
            std::cout << "     Likely Cause      : " << rec.llmResponse.likelyCause << "\n";
            std::cout << "     Next Action       : " << rec.llmResponse.suggestedNextSteps << "\n";
        } else {
            std::cout << " [✓] FAST PATH ROUTE   : Verified Routine Event. Stored locally (Cost: $0.00, Time: " 
                      << std::fixed << std::setprecision(2) << rec.processingTimeMicroseconds << " µs)\n";
        }
    }

    printDivider();
    EngineMetrics m = engine.getMetrics();
    std::cout << "\n======================== EVALUATION & BENCHMARK SUMMARY ========================\n";
    std::cout << " Total Logs Processed       : " << m.totalLogsProcessed << "\n";
    std::cout << " DFA Accepted (Fast Path)   : " << m.dfaAcceptedCount << " (" 
              << (m.totalLogsProcessed ? (m.dfaAcceptedCount * 100 / m.totalLogsProcessed) : 0) << "%)\n";
    std::cout << " DFA Rejected (Anomalies)   : " << m.dfaRejectedCount << "\n";
    std::cout << " Moore Machine Flagged      : " << m.mooreFlaggedCount << "\n";
    std::cout << " Total Escalated to LLM     : " << m.escalatedCount << " (" 
              << (m.totalLogsProcessed ? (m.escalatedCount * 100 / m.totalLogsProcessed) : 0) << "%)\n";
    std::cout << " Turing Machine Masked Chars: " << m.totalTMMaskedChars << " chars\n";
    std::cout << " Average Latency per Log    : " 
              << (m.totalLogsProcessed ? (m.totalLatencyMicroseconds / m.totalLogsProcessed) : 0.0) 
              << " microseconds\n";
    std::cout << " Estimated API Cost Saved   : $" << std::fixed << std::setprecision(4) 
              << m.simulatedCostSavedUSD << " USD (vs 100% LLM baseline)\n";
    std::cout << "================================================================================\n\n";

    return 0;
}
