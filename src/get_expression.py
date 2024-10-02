import re
import sympy as sp

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
            term = re.sub(r'\((\w+)\)\*\(\1\)', r'\1^2', term)
        elif re.search(r'\((\w+)\)\*\((\w+)\)', term):
            term = re.sub(r'\((\w+)\)\*\((\w+)\)', r'\1*\2', term)
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

def expression_to_matrix(expressions: list):
    matrix = []
    rhs_values = []
    for expr in expressions:
        lhs, rhs = expr.split('=')
        lhs = lhs.strip()
        rhs = rhs.strip()
        equation = sp.sympify(lhs)
        variables = sorted(equation.free_symbols, key=lambda x: x.name)
        coefficients = [equation.coeff(var) for var in variables]
        matrix.append(coefficients)
        rhs_values.append(float(rhs))
    return matrix, rhs_values

def get_expression_from_matrix(matrix):
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

