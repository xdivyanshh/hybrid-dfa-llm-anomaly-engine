#include "moore.hpp"

std::string MooreResult::stateToString(MooreState state) {
    switch (state) {
        case MooreState::M0: return "m0";
        case MooreState::M1: return "m1";
        case MooreState::M2: return "m2";
        case MooreState::M3: return "m3";
        default:             return "mUnknown";
    }
}

std::string MooreResult::outputToString(MooreOutput output) {
    switch (output) {
        case MooreOutput::OK:   return "OK";
        case MooreOutput::FLAG: return "FLAG";
        default:                return "UNKNOWN";
    }
}

MooreMachine::MooreMachine() {}

MooreOutput MooreMachine::getOutput(MooreState state) {
    // Moore Machine output depends strictly on the current state (Figure 3)
    if (state == MooreState::M3) {
        return MooreOutput::FLAG;
    }
    return MooreOutput::OK;
}

MooreState MooreMachine::transition(MooreState current, bool isSuccess) {
    if (isSuccess) {
        // Any Success resets counter back to m0
        return MooreState::M0;
    }

    // On Failed: m0 -> m1 -> m2 -> m3 -> m3
    switch (current) {
        case MooreState::M0: return MooreState::M1;
        case MooreState::M1: return MooreState::M2;
        case MooreState::M2: return MooreState::M3;
        case MooreState::M3: return MooreState::M3;
        default:             return MooreState::M0;
    }
}

MooreState MooreMachine::getState(const std::string& ip) const {
    auto it = ipStates_.find(ip);
    if (it != ipStates_.end()) {
        return it->second;
    }
    return MooreState::M0; // Default start state
}

void MooreMachine::reset(const std::string& ip) {
    ipStates_[ip] = MooreState::M0;
}

MooreResult MooreMachine::processEvent(const std::string& ip, const std::string& status) {
    MooreState prev = getState(ip);
    bool isSuccess = (status == "Success");
    MooreState current = transition(prev, isSuccess);
    ipStates_[ip] = current;

    MooreResult result;
    result.ip = ip;
    result.previousState = prev;
    result.currentState = current;
    result.output = getOutput(current);

    switch (current) {
        case MooreState::M0: result.consecutiveFailures = 0; break;
        case MooreState::M1: result.consecutiveFailures = 1; break;
        case MooreState::M2: result.consecutiveFailures = 2; break;
        case MooreState::M3: result.consecutiveFailures = 3; break;
    }

    result.statePath = {MooreResult::stateToString(prev), MooreResult::stateToString(current)};
    return result;
}
