import itertools
import string
import math

def generate_variable_names():
    alphabet = string.ascii_lowercase
    for length in range(1, 3):
        for name in itertools.product(alphabet, repeat=length):
            yield ''.join(name)

def create_l(size):
    var_names = generate_variable_names()
    matrix_ = []
    for i in range(size):
        matrix_row = []
        for j in range(size):
            if j <= i:
                matrix_row.append(next(var_names))
            else:
                matrix_row.append(0)
        matrix_.append(matrix_row)
    return matrix_

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

def create_ll(size):
    original_matrix = create_l(size)
    flipped_matrix = transpose(original_matrix)
    return [original_matrix, flipped_matrix]

def dict_to_triangular_matrix(value_dict):
    num_elements = len(value_dict)
    rows = math.ceil(math.sqrt(num_elements))
    cols = rows
    matrix = [[0] * cols for _ in range(rows)]
    keys = sorted(value_dict.keys())
    index = 0
    for i in range(rows):
        for j in range(i + 1):
            if index < len(keys):
                matrix[i][j] = value_dict[keys[index]]
                index += 1
            else:
                matrix[i][j] = 0
    return matrix