from algebra.matrices import Matrix

def print_matrix():
    print(Matrix([[0, 1, 2], [0, 3, 5]]))

def print_matrix_transpose():
    print(Matrix([[0, 1, 2], [0, 3, 5]]).transpose())


if __name__ == '__main__':
    print_matrix()
    print_matrix_transpose()