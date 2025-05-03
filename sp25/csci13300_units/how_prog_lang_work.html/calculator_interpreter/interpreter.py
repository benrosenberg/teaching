import lexer
import parser
import ast_types


def process_ast_exp(ast: ast_types.ASTNode):
    result = None
    match type(ast):
        case ast_types.Number:
            result = process_number(ast)
        case ast_types.NegExp:
            result = process_neg_exp(ast)
        case ast_types.AddExp:
            result = process_add_exp(ast)
        case ast_types.SubExp:
            result = process_sub_exp(ast)
        case ast_types.MulExp:
            result = process_mul_exp(ast)
        case ast_types.DivExp:
            result = process_div_exp(ast)
    if result is None:
        raise SyntaxError("Unable to process AST of type {}".format(type(ast)))
    return result


def process_add_exp(ast):
    a = process_ast_exp(ast.left)
    b = process_ast_exp(ast.right)
    return a + b


def process_sub_exp(ast):
    a = process_ast_exp(ast.left)
    b = process_ast_exp(ast.right)
    return a - b


def process_mul_exp(ast):
    a = process_ast_exp(ast.left)
    b = process_ast_exp(ast.right)
    return a * b


def process_div_exp(ast):
    a = process_ast_exp(ast.left)
    b = process_ast_exp(ast.right)
    if b == 0:
        raise ZeroDivisionError(f"Zero division error: cannot divide {a} by 0")
    return int(a / b)


def process_neg_exp(ast):
    result = process_ast_exp(ast.data)
    return -result


def process_number(ast: ast_types.Number):
    try:
        return int(ast.data)
    except:
        raise SyntaxError('Unable to process "{}" as number'.format(ast.data))


def interpret(source_code, verbose=False):
    try:
        lexemes = lexer.lex(source_code)
        if verbose:
            print("Lexemes:")
            print(lexemes)
        try:
            ast = parser.parse(lexemes)
            if verbose:
                print("AST:")
                print(ast)
            try:
                return process_ast_exp(ast)
            except Exception as e:
                if verbose:
                    print("Encountered interpreting error: {}".format(repr(e)))
                    print("Returning None")
                return None
        except Exception as e:
            if verbose:
                print("Encountered parsing error: {}".format(repr(e)))
                print("Returning None")
            return None
    except Exception as e:
        if verbose:
            print("Encountered lexing error: {}".format(repr(e)))
            print("Returning None")
        return None
