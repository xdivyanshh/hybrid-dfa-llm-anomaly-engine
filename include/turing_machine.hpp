#pragma once

#include <string>
#include <vector>
#include <memory>

enum class TMState {
    Q_SCAN,    // Scanning right for sensitive keyword boundaries
    Q_MATCH,   // Matching candidate sensitive keyword characters
    Q_MASK,    // Overwriting sensitive payload values with 'X'
    Q_HALT     // Reached end of tape (Blank symbol B)
};

enum class MoveDirection {
    LEFT,
    RIGHT,
    STAY
};

struct TMStepLog {
    int stepNumber;
    std::string state;
    size_t headPosition;
    char readSymbol;
    char writtenSymbol;
    char direction; // 'L', 'R', 'S'
};

struct TMExecutionResult {
    std::string originalTape;
    std::string sanitizedTape;
    int totalSteps;
    int maskedCharacters;
    std::vector<TMStepLog> stepTrace; // First N steps for audit/display
    bool halted;
};

class TuringMachineSanitizer {
public:
    static constexpr char BLANK = '\0';
    static constexpr char MASK_CHAR = 'X';

    TuringMachineSanitizer();

    // Loads a raw string onto the tape, runs the 7-tuple TM, and returns sanitized result
    TMExecutionResult sanitize(const std::string& input);

    static std::string stateToString(TMState state);

private:
    // Tape operations
    char readTape(const std::vector<char>& tape, size_t pos) const;
    void writeTape(std::vector<char>& tape, size_t pos, char val);
};
