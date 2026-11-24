#pragma once

#include "lexer.hpp"
#include "dfa.hpp"
#include "moore.hpp"
#include "turing_machine.hpp"
#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
#include <chrono>

struct LLMEscalationPayload {
    std::string eventType;
    std::string rawLog;
    std::string sanitizedLog;
    std::string dfaResult;
    std::vector<std::string> visitedStates;
    std::string lastValidState;
    std::string reason;
    std::vector<std::string> sessionContext;
    int tmSteps;
    int tmMaskedChars;

    std::string toJSON() const;
};

struct LLMResponse {
    std::string severity;
    std::string likelyCause;
    std::string evidence;
    double confidence;
    std::string suggestedNextSteps;
    bool schemaValid;
};

struct EventProcessRecord {
    std::string rawLine;
    bool dfaAccepted;
    DFAResult dfaResult;
    bool mooreFlagged;
    MooreResult mooreResult;
    bool escalated;
    LLMEscalationPayload escalationPayload;
    LLMResponse llmResponse;
    double processingTimeMicroseconds;
};

struct EngineMetrics {
    size_t totalLogsProcessed = 0;
    size_t dfaAcceptedCount = 0;
    size_t dfaRejectedCount = 0;
    size_t mooreFlaggedCount = 0;
    size_t escalatedCount = 0;
    size_t totalTMMaskedChars = 0;
    double totalLatencyMicroseconds = 0.0;
    double simulatedCostSavedUSD = 0.0;
};

class AnomalyEngine {
public:
    explicit AnomalyEngine(size_t maxQueueCapacity = 1000);

    // Process a single log event through the full neuro-symbolic pipeline
    EventProcessRecord processLine(const std::string& line);

    // Process a batch/file of logs
    std::vector<EventProcessRecord> processBatch(const std::vector<std::string>& lines);

    // Returns cumulative metrics
    EngineMetrics getMetrics() const { return metrics_; }

    // Simulates / executes LLM analysis on an escalation payload
    LLMResponse analyzeWithLLM(const LLMEscalationPayload& payload);

private:
    Lexer lexer_;
    BaselineDFA dfa_;
    MooreMachine moore_;
    TuringMachineSanitizer tmSanitizer_;
    size_t maxQueueCapacity_;
    std::queue<LLMEscalationPayload> escalationQueue_;
    std::unordered_map<std::string, std::vector<std::string>> recentIpHistory_;
    EngineMetrics metrics_;
};
