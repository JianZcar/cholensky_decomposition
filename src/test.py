from create_matrix import *
from get_expression import *
from compute import *

expressions = [
    "4*a + 10*b + 8*c = 44",
    "10*a + 26*b + 26*c = 128",
    "8*a + 26*b + 61*c = 214"
]

# Convert expressions to matrix form
lhs_matrix, rhs_values = expression_to_matrix(expressions)
print("LHS Matrix:")
for row in lhs_matrix:
    print(row)
print("RHS Values:", rhs_values)

# Create original and flipped matrices
size = 3
original_matrix, flipped_matrix = create_ll(size)

# Calculate the result matrix from original and flipped matrices
result_matrix = string_exp_matrix_calc(original_matrix, flipped_matrix)

# Simplify the result matrix
simplified_result_matrix = simplify_matrix(result_matrix)
print("\nSimplified Result Matrix:")
for row in simplified_result_matrix:
    print(row)

# Equate the matrices and solve for variables
solutions_dict = equate_matrices(lhs_matrix, simplified_result_matrix)
print("Solutions Dictionary:", solutions_dict)

# Convert the solutions dictionary to a triangular matrix
triangular_matrix = dict_to_triangular_matrix(solutions_dict)
print("\nTriangular Matrix:")
for row in triangular_matrix:
    print(row)

# Transpose the triangular matrix
transposed_triangular_matrix = transpose(triangular_matrix)
print("\nTransposed Triangular Matrix:")
for row in transposed_triangular_matrix:
    print(row)

# Get expressions from the triangular matrix
triangular_expressions = get_expression_from_matrix(triangular_matrix)
print("\nTriangular Expressions:")
for i, expr in enumerate(triangular_expressions):
    print(f'{expr} = {rhs_values[i]}')

# Solve for the variables using the triangular expressions
triangular_solutions = solve_for_t_matrix(triangular_expressions, rhs_values)
print("Triangular Solutions:", triangular_solutions)

# Prepare for solving the transposed matrix
transposed_rhs_values = list(triangular_solutions.values())
transposed_expressions = get_expression_from_matrix(transposed_triangular_matrix)
print("\nTransposed Expressions:")
for i, expr in enumerate(transposed_expressions):
    print(f'{expr} = {transposed_rhs_values[i]}')

# Solve for the variables using the transposed expressions
transposed_solutions = solve_for_t_matrix(transposed_expressions, transposed_rhs_values, True)
print("Transposed Solutions:", transposed_solutions)
