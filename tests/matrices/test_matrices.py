from algebra.matrices import Matrix

def test_matrix_creation():
    x = Matrix([[0, 1, 2], [0, 3, 5]])
    assert x.data == [[0, 1, 2], [0, 3, 5]]

def test_matrix_with_strings():
    try:
        Matrix([["8", 1, 2], [0, 3, 5]])
        assert False
    except TypeError:
        assert True

def test_matrix_with_uneven_rows():
    try:
        Matrix([[1, 2], [0, 3, 5]])
        assert False
    except ValueError:
        assert True

def test_matrix_transpose():
    X = Matrix([[0, 1, 2], [0, 3, 5]])
    X_T = X.transpose()
    assert X_T == Matrix([[0, 0], [1, 3], [2, 5]])

def test_matrix_addition():
    A = Matrix([[0, 1, 2], [0, 3, 5]])
    B = Matrix([[0, 1, 2], [0, 3, 5]])
    assert A.add(B) == Matrix([[0, 2, 4], [0, 6, 10]])

def test_matrix_substraction():
    A = Matrix([[0, 1, 2], [0, 3, 5]])
    B = Matrix([[0, 1, 2], [0, 3, 5]])
    assert A.substract(B) == Matrix([[0, 0, 0], [0, 0, 0]])

def test_matrix_scalar_multiplication():
    A = Matrix([[0, 1, 2], [0, 3, 5]])
    assert A.scalar_multiply(2) == Matrix([[0, 2, 4], [0, 6, 10]])



if __name__ == '__main__':
    test_matrix_creation()
    test_matrix_with_strings()
    test_matrix_with_uneven_rows()
    test_matrix_transpose()
    test_matrix_addition()
    test_matrix_substraction()
    test_matrix_scalar_multiplication()
    

    print("All tests passed. ✅")
