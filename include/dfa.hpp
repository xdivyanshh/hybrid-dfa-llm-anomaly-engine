#pragma once

#include "lexer.hpp"
#include <string>
#include <vector>

enum class DFAState {
    Q0, // Start state
    Q1, // Received LEVEL
    Q2, // Received IP
    Q3, // Received USER
    Q4, // Final state: Received STATUS
    QE  // Trap / Dead state
};

enum class DFAVerdict {
    ACCEPT,
    REJECT
};

struct DFAResult {
    DFAVerdict verdict;
    std::vector<std::string> visitedStates;
    std::string lastValidState;
    std::string reason;
    int failedPosition; // -1 if accepted

    static std::string stateToString(DFAState state);
};

class BaselineDFA {
public:
    BaselineDFA();

    // Runs the DFA on a sequence of tokens according to Table 3 transition function
    DFAResult process(const std::vector<Token>& tokens);

    // Transition function delta(state, token_type)
    static DFAState transition(DFAState current, TokenType token);

    static bool isFinal(DFAState state) {
        return state == DFAState::Q4;
    }

    static bool isTrap(DFAState state) {
        return state == DFAState::QE;
    }
};
