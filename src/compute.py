from create_matrix import *
from get_expression import *
import sympy as sp
import re

def extract_symbols(string):
    symbols_set = set()
    symbols_set.update(re.findall(r'[a-zA-Z]+', string))
    return symbols_set

def equate_matrices(matrix_a, matrix_b):
    value_dict = dict()
    size = len(matrix_a)
    equations = []

    for i in range(size):
        for j in range(size):
            value = matrix_a[i][j]
            expression = matrix_b[i][j]
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
            else:
                pass
    return value_dict

matrix1 = [
    [4, 10, 8],
    [10, 26, 26],
    [8, 26, 61],
]
size = 3
original_matrix, flipped_matrix = create_ll(size)
result_matrix = string_exp_matrix_calc(original_matrix, flipped_matrix)

simplified_matrix = simplify_matrix(result_matrix)

matrix2 = simplified_matrix
print("\nSimplified Matrix:")
for row in simplified_matrix:
    print(row)

solutions = equate_matrices(matrix1, matrix2)
print(solutions)
matrix = dict_to_triangular_matrix(solutions)
for row in matrix:
    print(row)
print('Transpose')
transposed_matrix = transpose(matrix)
for row in transposed_matrix:
    print(row)