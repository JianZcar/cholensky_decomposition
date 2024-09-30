# from objects import *
import itertools
import string

def generate_variable_names():
    alphabet = string.ascii_lowercase
    for length in range(1, 3):  # Adjust range for more letters if needed
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

def create_ll(size):
    original_matrix = create_l(size)
    flipped_matrix = [[original_matrix[j][i] for j in range(size)] for i in range(size)]
    return [original_matrix, flipped_matrix]
if __name__ == "__main__":
    print('Test')
    # matrix = create_l(4)
    # for row in matrix:
    #     print([var for var in row])

    matrices = create_ll(4)
    for matrix in matrices:
        for row in matrix:
            print([var for var in row])
        print()