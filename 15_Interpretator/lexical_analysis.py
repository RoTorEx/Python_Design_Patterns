from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


def lex(input):
    result = []

    i = 0
    while i < len(input):
        if input[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif input[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif input[i] == "(":
            result.append(Token(Token.Type.LPAREN, "("))
        elif input[i] == ")":
            result.append(Token(Token.Type.RPAREN, ")"))
        else:  # must be a number
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, "".join(digits)))
                    break
        i += 1

    return result


def calc(input):
    tokens = lex(input)
    print(" ".join(map(str, tokens)))


if __name__ == "__main__":
    calc("(13+4)-(12+1)")
