LPAREN = r"("
RPAREN = r")"
DIGIT = r"\d"
OPPLUS = r"+"
OPMINUS = r"-"
OPMUL = r"*"
OPDIV = r"/"
WHITESPACE = r"\s"

constants = [LPAREN, RPAREN, OPPLUS, OPMINUS, OPMUL, OPDIV]


def skip_whitespace(s, idx):
    while s[idx] in ' \t\r\n':
        idx += 1
    return idx


def lex(source_code):
    lexemes = []
    i = 0
    while i < len(source_code):
        i = skip_whitespace(source_code, i)
        if source_code[i] in constants:
            lexemes.append(source_code[i])
        elif source_code[i].isdigit():
            num = source_code[i]
            i += 1
            while i < len(source_code) and source_code[i].isdigit():
                num += source_code[i]
                i += 1
            lexemes.append(num)
            # undo last increment
            i -= 1
        else:
            raise SyntaxError("Unknown character: {}".format(source_code[i]))
        i += 1
    return lexemes
