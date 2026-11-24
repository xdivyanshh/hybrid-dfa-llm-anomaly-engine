#pragma once

#include <string>
#include <unordered_map>
#include <vector>

enum class MooreState {
    M0, // 0 consecutive failures (Output: OK)
    M1, // 1 consecutive failure  (Output: OK)
    M2, // 2 consecutive failures (Output: OK)
    M3  // 3+ consecutive failures (Output: FLAG)
};

enum class MooreOutput {
    OK,
    FLAG
};

struct MooreResult {
    MooreOutput output;
    MooreState previousState;
    MooreState currentState;
    int consecutiveFailures;
    std::string ip;
    std::vector<std::string> statePath;

    static std::string stateToString(MooreState state);
    static std::string outputToString(MooreOutput output);
};

class MooreMachine {
public:
    MooreMachine();

    // Updates session state for a given IP with the login status ("Success" or "Failed")
    MooreResult processEvent(const std::string& ip, const std::string& status);

    // Get current state for an IP
    MooreState getState(const std::string& ip) const;

    // Reset monitor for an IP
    void reset(const std::string& ip);

    // Get output for a given state
    static MooreOutput getOutput(MooreState state);

    // Transition delta(current_state, isSuccess)
    static MooreState transition(MooreState current, bool isSuccess);

private:
    std::unordered_map<std::string, MooreState> ipStates_;
};
