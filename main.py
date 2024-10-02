from cli.input_cli import *
from cli.grid import *
from src.compute import *
from src.create_matrix import *
from src.get_expression import *
from src.verify import *
def main():
    equations = input_cli()
    print("Ax = B")
    variable_lhs = sorted(list(extract_symbols(equations[0])))
    lhs_matrix, rhs_values = expression_to_matrix(equations)
    lhs_display = generate_display_matrix(lhs_matrix)
    rhs_display = generate_display_list_with_border(rhs_values)
    variable_lhs_display = generate_display_list_with_border(variable_lhs)
    lhs_display_join = join_display(lhs_display, variable_lhs_display)
    lhs_display_join = join_display(lhs_display_join, generate_display_symbol(len(lhs_display_join)))
    lhs_display_join = join_display(lhs_display_join, rhs_display)
    render_grid(lhs_display_join)

    print("\nA = LL^T")
    size = len(equations)
    original_matrix, flipped_matrix = create_ll(size)
    result_matrix = string_exp_matrix_calc(original_matrix, flipped_matrix)
    simplified_result_matrix = simplify_matrix(result_matrix)
    display_original_matrix = generate_display_matrix(original_matrix)
    display_flipped_matrix = generate_display_matrix(flipped_matrix)
    display_result_matrix = generate_display_matrix(simplified_result_matrix)

    display_a_original_flipped_matrix = join_display(lhs_display, generate_display_symbol(len(lhs_display)))
    display_a_result_matrix = join_display(display_a_original_flipped_matrix, display_result_matrix)
    display_a_original_flipped_matrix = join_display(display_a_original_flipped_matrix, display_original_matrix)
    display_a_original_flipped_matrix = join_display(display_a_original_flipped_matrix, display_flipped_matrix)
    render_grid(display_a_original_flipped_matrix)
    render_grid(display_a_result_matrix)
    solutions_dict = equate_matrices(lhs_matrix, simplified_result_matrix)
    print(solutions_dict)

    print("\nLy = B")
    triangular_matrix = dict_to_triangular_matrix(solutions_dict)
    transposed_triangular_matrix = transpose(triangular_matrix)
    triangular_expressions = get_expression_from_matrix(triangular_matrix)
    display_triangular_matrix = generate_display_matrix(triangular_matrix)
    display_transposed_triangular_matrix = generate_display_matrix(transposed_triangular_matrix)
    display_triangular_matrix_join = join_display(display_triangular_matrix, variable_lhs_display)
    display_triangular_matrix_join = join_display(display_triangular_matrix_join, generate_display_symbol(len(display_triangular_matrix_join)))
    display_triangular_matrix_join = join_display(display_triangular_matrix_join, rhs_display)
    render_grid(display_triangular_matrix_join)
    print("\nExpressions:")
    for i, expr in enumerate(triangular_expressions):
        print(f'{expr} = {rhs_values[i]}')
    triangular_solutions = solve_for_t_matrix(triangular_expressions, rhs_values)
    print(triangular_solutions)

    print("\nL^Tx= y")
    transposed_rhs_values = list(triangular_solutions.values())
    transposed_expressions = get_expression_from_matrix(transposed_triangular_matrix)
    display_transposed_rhs_values = generate_display_list_with_border(transposed_rhs_values)
    display_transposed_triangular_matrix_join = join_display(display_transposed_triangular_matrix, variable_lhs_display)
    display_transposed_triangular_matrix_join = join_display(display_transposed_triangular_matrix_join, generate_display_symbol(len(display_transposed_triangular_matrix_join)))
    display_transposed_triangular_matrix_join = join_display(display_transposed_triangular_matrix_join, display_transposed_rhs_values)
    render_grid(display_transposed_triangular_matrix_join)

    print("\nExpressions:")
    for i, expr in enumerate(transposed_expressions):
        print(f'{expr} = {transposed_rhs_values[i]}')
    transposed_solutions = solve_for_t_matrix(transposed_expressions, transposed_rhs_values, True)
    print(transposed_solutions)

main()