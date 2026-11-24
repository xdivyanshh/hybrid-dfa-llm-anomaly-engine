#include "dfa.hpp"

std::string DFAResult::stateToString(DFAState state) {
    switch (state) {
        case DFAState::Q0: return "q0";
        case DFAState::Q1: return "q1";
        case DFAState::Q2: return "q2";
        case DFAState::Q3: return "q3";
        case DFAState::Q4: return "q4";
        case DFAState::QE: return "qE";
        default:           return "qUnknown";
    }
}

BaselineDFA::BaselineDFA() {}

DFAState BaselineDFA::transition(DFAState current, TokenType token) {
    // Total transition function delta from Table 3 (Minimal Baseline DFA)
    switch (current) {
        case DFAState::Q0:
            if (token == TokenType::LEVEL) return DFAState::Q1;
            return DFAState::QE;

        case DFAState::Q1:
            if (token == TokenType::IP) return DFAState::Q2;
            return DFAState::QE;

        case DFAState::Q2:
            if (token == TokenType::USER) return DFAState::Q3;
            return DFAState::QE;

        case DFAState::Q3:
            if (token == TokenType::STATUS) return DFAState::Q4;
            return DFAState::QE;

        case DFAState::Q4:
            // Any token after final state leads to trap state qE
            return DFAState::QE;

        case DFAState::QE:
        default:
            // Once in trap state qE, never leaves
            return DFAState::QE;
    }
}

DFAResult BaselineDFA::process(const std::vector<Token>& tokens) {
    DFAResult result;
    result.failedPosition = -1;
    DFAState current = DFAState::Q0;
    result.visitedStates.push_back(DFAResult::stateToString(current));
    result.lastValidState = DFAResult::stateToString(current);

    for (size_t i = 0; i < tokens.size(); ++i) {
        DFAState next = transition(current, tokens[i].type);
        result.visitedStates.push_back(DFAResult::stateToString(next));

        if (next == DFAState::QE && current != DFAState::QE) {
            result.failedPosition = static_cast<int>(i + 1); // 1-based token position
            result.reason = "unexpected token '" + tokens[i].value + "' (" +
                            Token::typeToString(tokens[i].type) + ") at position " +
                            std::to_string(result.failedPosition);
        } else if (next != DFAState::QE) {
            result.lastValidState = DFAResult::stateToString(next);
        }

        current = next;
    }

    if (current == DFAState::Q4) {
        result.verdict = DFAVerdict::ACCEPT;
        result.reason = "valid login structure accepted";
    } else {
        result.verdict = DFAVerdict::REJECT;
        if (result.reason.empty()) {
            if (tokens.empty()) {
                result.reason = "empty log line";
            } else {
                result.reason = "incomplete sequence (ended at state " +
                                DFAResult::stateToString(current) + ")";
            }
        }
    }

    return result;
}
