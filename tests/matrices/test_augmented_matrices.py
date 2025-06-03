from algebra.augmented_matrices import AugmentedMatrix
from algebra.matrices import Matrix
from algebra.vectors import Vector

def test_augmented_matrix_compatible_dimensions():
    A = Matrix([[1, 2], 
                [3, 4]])
    b = Vector([1, 2])
    Ab = Matrix([[1, 2, 1], 
                [3, 4, 2]])
    assert Ab == AugmentedMatrix(A, b)

def test_augmented_matrix_incompatible_dimensions():
    A = Matrix([[1, 2], [3, 4]])
    b = Vector([1, 2, 3])
    try:
        AugmentedMatrix(A, b)
        assert False
    except ValueError:
        assert True

if __name__ == '__main__':
    test_augmented_matrix_compatible_dimensions()
    test_augmented_matrix_incompatible_dimensions()
    print("All tests passed. ✅")