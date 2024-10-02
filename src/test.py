from create_matrix import *
from get_expression import *
from compute import *

expressions = [
    "4*a + 10*b + 8*c = 44",
    "10*a + 26*b + 26*c = 128",
    "8*a + 26*b + 61*c = 214"
]
matrix1, rhs_values = expression_to_matrix(expressions)
for row in matrix1:
    print(row)
print(rhs_values)
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

expressions = get_expression_for_ty_equal_b(matrix)
for i, expr in enumerate(expressions):
    print(f'{expr} = {rhs_values[i]}')

solutions = solve_for_ty_equal_b(expressions, rhs_values)
print(solutions)
