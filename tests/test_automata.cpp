#include "lexer.hpp"
#include "dfa.hpp"
#include "moore.hpp"
#include "turing_machine.hpp"
#include <iostream>
#include <cassert>

void testLexer() {
    Lexer lexer;
    assert(lexer.classifyLexeme("[INFO]") == TokenType::LEVEL);
    assert(lexer.classifyLexeme("192.168.1.50") == TokenType::IP);
    assert(lexer.classifyLexeme("256.1.1.1") == TokenType::OTHER); // Invalid IP octet > 255
    assert(lexer.classifyLexeme("User_Admin") == TokenType::USER);
    assert(lexer.classifyLexeme("Admin") == TokenType::OTHER);      // Missing User_ prefix
    assert(lexer.classifyLexeme("Success") == TokenType::STATUS);
    assert(lexer.classifyLexeme("Failed") == TokenType::STATUS);
    assert(lexer.classifyLexeme("DROP_TABLE") == TokenType::OTHER);
    std::cout << "[✓] testLexer passed.\n";
}

void testDFA() {
    Lexer lexer;
    BaselineDFA dfa;

    // Case A from Table 4 of Synopsis: Valid line
    auto tokensA = lexer.tokenize("[INFO] 192.168.1.50 User_Admin Success");
    auto resA = dfa.process(tokensA);
    assert(resA.verdict == DFAVerdict::ACCEPT);
    assert(resA.visitedStates.back() == "q4");

    // Case B from Table 4 of Synopsis: Injected OTHER token
    auto tokensB = lexer.tokenize("[INFO] 192.168.1.50 DROP_TABLE User Success");
    auto resB = dfa.process(tokensB);
    assert(resB.verdict == DFAVerdict::REJECT);
    assert(resB.visitedStates.back() == "qE");
    assert(resB.lastValidState == "q2");

    // Incomplete line
    auto tokensInc = lexer.tokenize("[INFO] 192.168.1.50");
    auto resInc = dfa.process(tokensInc);
    assert(resInc.verdict == DFAVerdict::REJECT);
    assert(resInc.lastValidState == "q2");

    std::cout << "[✓] testDFA passed (Table 4 Worked Examples verified).\n";
}

void testMooreMachine() {
    MooreMachine moore;
    std::string ip = "192.168.1.52";

    // 1st failure: m0 -> m1 (OK)
    auto r1 = moore.processEvent(ip, "Failed");
    assert(r1.currentState == MooreState::M1);
    assert(r1.output == MooreOutput::OK);

    // 2nd failure: m1 -> m2 (OK)
    auto r2 = moore.processEvent(ip, "Failed");
    assert(r2.currentState == MooreState::M2);
    assert(r2.output == MooreOutput::OK);

    // 3rd failure: m2 -> m3 (FLAG)
    auto r3 = moore.processEvent(ip, "Failed");
    assert(r3.currentState == MooreState::M3);
    assert(r3.output == MooreOutput::FLAG);

    // 4th failure: stays at m3 (FLAG)
    auto r4 = moore.processEvent(ip, "Failed");
    assert(r4.currentState == MooreState::M3);
    assert(r4.output == MooreOutput::FLAG);

    // Success resets back to m0 (OK)
    auto r5 = moore.processEvent(ip, "Success");
    assert(r5.currentState == MooreState::M0);
    assert(r5.output == MooreOutput::OK);

    std::cout << "[✓] testMooreMachine passed (Figure 3 State Transducer verified).\n";
}

void testTuringMachine() {
    TuringMachineSanitizer tm;

    // Test masking sensitive credentials on tape
    std::string raw = "User_Guest pass=SecretPassword999 Failed";
    auto res = tm.sanitize(raw);
    assert(res.halted == true);
    assert(res.maskedCharacters == 17);
    assert(res.sanitizedTape == "User_Guest pass=XXXXXXXXXXXXXXXXX Failed");

    // Test token masking
    std::string raw2 = "auth token=api_key_123456";
    auto res2 = tm.sanitize(raw2);
    assert(res2.maskedCharacters == 14);
    assert(res2.sanitizedTape == "auth token=XXXXXXXXXXXXXX");

    std::cout << "[✓] testTuringMachine passed (7-tuple TM Tape Masker verified).\n";
}

int main() {
    std::cout << "==================================================\n";
    std::cout << " RUNNING AUTOMATA UNIT TESTS (THEORY OF COMPUTATION)\n";
    std::cout << "==================================================\n";
    testLexer();
    testDFA();
    testMooreMachine();
    testTuringMachine();
    std::cout << "==================================================\n";
    std::cout << " ALL AUTOMATA SPECIFICATIONS VERIFIED 100% CORRECT\n";
    std::cout << "==================================================\n";
    return 0;
}
