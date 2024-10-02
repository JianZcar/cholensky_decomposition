import sympy as sp
import re

from mpmath.libmp.libintmath import ifac2


def extract_symbols(string):
    string = str(string)
    symbols_set = set()
    symbols_set.update(re.findall(r'[a-zA-Z]+', string))
    return symbols_set

def solve_expression(expression, value, value_dict):
    symbols_set = extract_symbols(expression)
    variables = sp.symbols(' '.join(symbols_set))
    if isinstance(variables, tuple):
        variables_dict = {str(var): var for var in variables}
    else:
        variables_dict = {str(variables): variables}
    expr = sp.sympify(expression, locals=variables_dict)
    for var, val in value_dict.items():
        expr = expr.subs(var, val)
        variables_dict.pop(var, None)
    eq = sp.Eq(value, expr)
    solved = sp.solve(eq, list(variables_dict.values()))
    if len(solved) > 1:
        value_dict[list(variables_dict.keys())[0]] = solved[1]
    elif len(solved) == 1:
        value_dict[list(variables_dict.keys())[0]] = solved[0]
    return value_dict

def equate_matrices(matrix_a, matrix_b):
    value_dict = dict()
    size = len(matrix_a)

    for i in range(size):
        for j in range(size):
            value = matrix_a[i][j]
            expression = matrix_b[i][j]
            value_dict = solve_expression(expression, value, value_dict)
    return value_dict

def solve_for_t_matrix(expressions, b, transposed=False):
    value_dict = dict()
    expressions = expressions[::-1] if transposed else expressions
    b = b[::-1] if transposed else b
    size = len(expressions)
    for i in range(size):
        value = b[i]
        expression = expressions[i]
        value_dict = solve_expression(expression, value, value_dict)
    return value_dict