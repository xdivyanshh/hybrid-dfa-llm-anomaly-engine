#pragma once

#include <string>
#include <vector>

enum class TokenType {
    LEVEL,
    IP,
    USER,
    STATUS,
    OTHER
};

struct Token {
    TokenType type;
    std::string value;

    static std::string typeToString(TokenType type);
};

class Lexer {
public:
    Lexer();
    std::vector<Token> tokenize(const std::string& line);
    TokenType classifyLexeme(const std::string& lexeme) const;

private:
    std::vector<std::string> split(const std::string& line) const;
};
