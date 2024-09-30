import numpy as np
def is_square(matrix):
    return len(matrix) == sum([len(row) for row in matrix])/len(matrix)

def is_symmetric(matrix):
    return matrix == [list(row) for row in zip(*matrix)]

def is_positive_definite(matrix):
    return all([eigenvalue > 0 for eigenvalue in np.linalg.eigvals(matrix)])

if __name__ == "__main__":
    print(is_square([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]]))  # True
    print(is_square([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15]]))  # False
    print(is_symmetric([[1, 2, 3, 4],
                        [2, 1, 4, 3],
                        [3, 4, 1, 2],
                        [4, 3, 2, 1]]))  # True
    print(is_symmetric([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]]))  # False
    print(is_positive_definite([[2, -1, 0],
                                [-1, 2, -1],
                                [0, -1, 2]]))  # True
    print(is_positive_definite([[1, 2],
                                [2, 1]])) # False