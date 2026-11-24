#include "turing_machine.hpp"
#include <algorithm>
#include <cctype>

constexpr char TuringMachineSanitizer::BLANK;
constexpr char TuringMachineSanitizer::MASK_CHAR;

std::string TuringMachineSanitizer::stateToString(TMState state) {
    switch (state) {
        case TMState::Q_SCAN:  return "q_scan";
        case TMState::Q_MATCH: return "q_match";
        case TMState::Q_MASK:  return "q_mask";
        case TMState::Q_HALT:  return "q_halt";
        default:               return "q_unknown";
    }
}

TuringMachineSanitizer::TuringMachineSanitizer() {}

char TuringMachineSanitizer::readTape(const std::vector<char>& tape, size_t pos) const {
    if (pos < tape.size()) {
        return tape[pos];
    }
    return BLANK;
}

void TuringMachineSanitizer::writeTape(std::vector<char>& tape, size_t pos, char val) {
    if (pos >= tape.size()) {
        tape.resize(pos + 1, BLANK);
    }
    tape[pos] = val;
}

TMExecutionResult TuringMachineSanitizer::sanitize(const std::string& input) {
    TMExecutionResult result;
    result.originalTape = input;
    result.totalSteps = 0;
    result.maskedCharacters = 0;
    result.halted = false;

    // Initialize tape with input symbols + trailing blank symbol B
    std::vector<char> tape(input.begin(), input.end());
    tape.push_back(BLANK);

    size_t head = 0;
    TMState state = TMState::Q_SCAN;

    // Patterns to trigger q_mask
    const std::vector<std::string> triggers = {
        "pass=", "password=", "pwd=", "token=", "secret=", "key=", "bearer "
    };

    auto checkTriggerAt = [&](size_t pos, size_t& triggerLen) -> bool {
        for (const auto& trig : triggers) {
            if (pos + trig.size() <= tape.size()) {
                bool match = true;
                for (size_t k = 0; k < trig.size(); ++k) {
                    if (std::tolower(static_cast<unsigned char>(tape[pos + k])) != trig[k]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    triggerLen = trig.size();
                    return true;
                }
            }
        }
        return false;
    };

    size_t triggerLength = 0;

    // Run Turing Machine simulation
    while (state != TMState::Q_HALT) {
        result.totalSteps++;
        char readSym = readTape(tape, head);
        char writeSym = readSym;
        char dir = 'R';
        TMState nextState = state;

        switch (state) {
            case TMState::Q_SCAN:
                if (readSym == BLANK) {
                    nextState = TMState::Q_HALT;
                    dir = 'S';
                } else if (checkTriggerAt(head, triggerLength)) {
                    // Match found: transition to Q_MATCH to skip prefix, then Q_MASK
                    nextState = TMState::Q_MASK;
                    head += triggerLength; // Move head past key=
                    readSym = readTape(tape, head);
                    writeSym = readSym;
                    if (readSym != BLANK && readSym != ' ' && readSym != '"' && readSym != ';' && readSym != '\'') {
                        writeSym = MASK_CHAR;
                        writeTape(tape, head, MASK_CHAR);
                        result.maskedCharacters++;
                    } else if (readSym == BLANK) {
                        nextState = TMState::Q_HALT;
                        dir = 'S';
                    }
                }
                break;

            case TMState::Q_MASK:
                if (readSym == BLANK) {
                    nextState = TMState::Q_HALT;
                    dir = 'S';
                } else if (readSym == ' ' || readSym == '"' || readSym == ';' || readSym == '\'' || readSym == '&') {
                    // Delimiter reached: stop masking, transition back to Q_SCAN
                    nextState = TMState::Q_SCAN;
                    writeSym = readSym; // Keep delimiter intact
                } else {
                    // Overwrite sensitive character with 'X' on tape
                    writeSym = MASK_CHAR;
                    writeTape(tape, head, MASK_CHAR);
                    result.maskedCharacters++;
                }
                break;

            case TMState::Q_HALT:
            default:
                dir = 'S';
                break;
        }

        // Record step log (keep first 30 steps for audit trail)
        if (result.stepTrace.size() < 30) {
            TMStepLog log;
            log.stepNumber = result.totalSteps;
            log.state = stateToString(state);
            log.headPosition = head;
            log.readSymbol = (readSym == BLANK ? 'B' : readSym);
            log.writtenSymbol = (writeSym == BLANK ? 'B' : writeSym);
            log.direction = dir;
            result.stepTrace.push_back(log);
        }

        state = nextState;
        if (dir == 'R') {
            head++;
        } else if (dir == 'L' && head > 0) {
            head--;
        }

        // Safety bound to avoid infinite loop
        if (result.totalSteps > 100000) {
            break;
        }
    }

    result.halted = (state == TMState::Q_HALT);

    // Convert tape back to string (excluding trailing blank)
    std::string sanitized = "";
    for (char c : tape) {
        if (c == BLANK) break;
        sanitized += c;
    }
    result.sanitizedTape = sanitized;

    return result;
}
