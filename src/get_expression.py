from create_matrix import *
import re

def string_exp_matrix_calc(matrix_a, matrix_b):
    size = len(matrix_a)
    result_matrix = []
    for i in range(size):
        result_row = []
        for j in range(size):
            expr = []
            for k in range(size):
                expr.append(f"({matrix_a[i][k]})*({matrix_b[k][j]})")
            result_row.append('+'.join(expr))
        result_matrix.append(result_row)
    return result_matrix

def simplify_expression(expr):
    terms = expr.split('+')
    simplified_terms = []
    for term in terms:
        if re.search(r'\*\(0\)', term):
            continue
        elif re.search(r'\(\w+\)\*\(0\)|\(0\)\*\(\w+\)', term):
            continue
        elif re.search(r'\((\w+)\)\*\(\1\)', term):
            term = re.sub(r'\((\w+)\)\*\(\1\)', r'(\1**2)', term)
        elif re.search(r'\((\w+)\)\*\((\w+)\)', term):
            term = re.sub(r'\((\w+)\)\*\((\w+)\)', r'(\1*\2)', term)
        simplified_terms.append(term)
    return '+'.join(simplified_terms)


def simplify_matrix(matrix):
    size = len(matrix)
    simplified_matrix = []
    for i in range(size):
        simplified_row = []
        for j in range(size):
            simplified_expr = simplify_expression(matrix[i][j])
            simplified_row.append(simplified_expr)
        simplified_matrix.append(simplified_row)
    return simplified_matrix

if __name__ == "__main__":
    size = 3
    original_matrix, flipped_matrix = create_ll(size)

    print("Original Matrix:")
    for row in original_matrix:
        print(row)

    print("\nFlipped Matrix:")
    for row in flipped_matrix:
        print(row)

    result_matrix = string_exp_matrix_calc(original_matrix, flipped_matrix)

    print("\nResult Matrix:")
    for row in result_matrix:
        print(row)

    simplified_matrix = simplify_matrix(result_matrix)

    print("\nSimplified Matrix:")
    for row in simplified_matrix:
        print(row)