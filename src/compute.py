import sympy as sp
import re

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

def get_expression_for_ty_equal_b(matrix):
    variables = {}
    expressions = []

    for i in range(len(matrix)):
        expr = 0
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                var_name = chr(97 + j)
                if var_name not in variables:
                    variables[var_name] = sp.symbols(var_name)
                expr += matrix[i][j] * variables[var_name]
        expressions.append(expr)

    return expressions

def solve_for_ty_equal_b(expressions, b):
    value_dict = dict()
    size = len(expressions)
    for i in range(size):
        value = b[i]
        expression = expressions[i]
        print(expression)
        value_dict = solve_expression(expression, value, value_dict)
    return value_dict