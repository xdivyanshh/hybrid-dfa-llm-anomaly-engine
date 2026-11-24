#include "lexer.hpp"
#include <sstream>
#include <regex>

std::string Token::typeToString(TokenType type) {
    switch (type) {
        case TokenType::LEVEL:  return "LEVEL";
        case TokenType::IP:     return "IP";
        case TokenType::USER:   return "USER";
        case TokenType::STATUS: return "STATUS";
        case TokenType::OTHER:  return "OTHER";
        default:                return "UNKNOWN";
    }
}

Lexer::Lexer() {}

std::vector<std::string> Lexer::split(const std::string& line) const {
    std::vector<std::string> tokens;
    std::istringstream iss(line);
    std::string token;
    while (iss >> token) {
        tokens.push_back(token);
    }
    return tokens;
}

TokenType Lexer::classifyLexeme(const std::string& lexeme) const {
    static const std::regex levelRegex(R"(^\[INFO\]$)");
    // IP octet: 25[0-5] | 2[0-4][0-9] | 1[0-9][0-9] | [1-9]?[0-9]
    static const std::string octet = R"((?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))";
    static const std::regex ipRegex("^" + octet + R"(\.)" + octet + R"(\.)" + octet + R"(\.)" + octet + "$");
    static const std::regex userRegex(R"(^User_[A-Za-z0-9]+$)");
    static const std::regex statusRegex(R"(^(Success|Failed)$)");

    if (std::regex_match(lexeme, levelRegex)) {
        return TokenType::LEVEL;
    }
    if (std::regex_match(lexeme, ipRegex)) {
        return TokenType::IP;
    }
    if (std::regex_match(lexeme, userRegex)) {
        return TokenType::USER;
    }
    if (std::regex_match(lexeme, statusRegex)) {
        return TokenType::STATUS;
    }
    return TokenType::OTHER;
}

std::vector<Token> Lexer::tokenize(const std::string& line) {
    std::vector<Token> result;
    std::vector<std::string> lexemes = split(line);
    for (const auto& lex : lexemes) {
        result.push_back({classifyLexeme(lex), lex});
    }
    return result;
}
