import ast_types
import lexer

"""
BNF grammar:

expression  ::= term (("+" | "-") term)*
term        ::= factor (("*" | "/") factor)*
factor      ::= "-" factor | "(" expression ")" | number
number      ::= digit (digit)*
digit       ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
"""

'''
Real BNF grammar for this parser:

expression  ::= term (("+" | "-") term)*
term        ::= factor (("*" | "/") factor)*
factor      ::= "-" factor | "(" expression ")" | number
'''


def parse(tokens):
    # entry point
    ast, next_pos = parse_expression(tokens, 0)
    if next_pos != len(tokens):
        raise SyntaxError(f"Unexpected token at end: {tokens[next_pos]}")
    return ast


def peek(tokens, pos):
    return tokens[pos] if pos < len(tokens) else None


# Expression := Term (("+"|"-") Term)*
def parse_expression(tokens, pos):
    node, pos = parse_term(tokens, pos)
    while True:
        tok = peek(tokens, pos)
        if tok == lexer.OPPLUS:
            pos += 1
            right, pos = parse_term(tokens, pos)
            node = ast_types.AddExp(node, right)
        elif tok == lexer.OPMINUS:
            pos += 1
            right, pos = parse_term(tokens, pos)
            node = ast_types.SubExp(node, right)
        else:
            break
    return node, pos


# Term := Factor (("*"|"/") Factor)*
def parse_term(tokens, pos):
    node, pos = parse_factor(tokens, pos)
    while True:
        tok = peek(tokens, pos)
        if tok == lexer.OPMUL:
            pos += 1
            right, pos = parse_factor(tokens, pos)
            node = ast_types.MulExp(node, right)
        elif tok == lexer.OPDIV:
            pos += 1
            right, pos = parse_factor(tokens, pos)
            node = ast_types.DivExp(node, right)
        else:
            break
    return node, pos


# Factor := "-" Factor | "(" Expression ")" | Number
def parse_factor(tokens, pos):
    tok = peek(tokens, pos)

    if tok == lexer.OPMINUS:
        pos += 1
        subexpr, pos = parse_factor(tokens, pos)
        return ast_types.NegExp(subexpr), pos

    if tok == lexer.LPAREN:
        pos += 1
        expr, pos = parse_expression(tokens, pos)
        if peek(tokens, pos) != lexer.RPAREN:
            raise SyntaxError("Expected {}".format(lexer.RPAREN))
        pos += 1
        return expr, pos

    if tok is not None and tok.isdigit():
        pos += 1
        return ast_types.Number(tok), pos

    raise SyntaxError(f"Unexpected token: {tok}")
