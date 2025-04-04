from algebra.vectors import Vector
from algebra.visualizer import LinearAlgebraVisualizer

def test_vector_creation():
    x = Vector([0, 1, 2])
    assert x.data == [0, 1, 2]

def test_vector_type_check():
    try:
        Vector((0, 1, 2))
        assert False
    except TypeError:
        assert True

def test_vector_dimensionality_check():
    try:
        Vector([[0, 1, 2]])
        assert False
    except TypeError:
        assert True

def test_vector_scalars_check():
    try:
        Vector(["a", True, 2])
        assert False
    except TypeError:
        assert True

def test_vector_length():
    assert Vector([0, 1, 2]).length == len([0, 1, 2]) == 3

def test_vector_3D_plot_error():
    try:
        LinearAlgebraVisualizer.plot_vector(Vector([1, 2, 3]))
        assert False
    except ValueError:
        assert True

def test_scalar_multiplication():
    assert Vector([0, 1, 2]).scalar_multiply(5) == Vector([0, 5, 10])

def test_scalar_multiplication_type_check():
    try:
        Vector([0, 1, 2]).scalar_multiply("10")
        assert False
    except TypeError:
        assert True

def test_vector_addition():
    assert Vector([0, 1, 2]).add(Vector([0, 1, 2])) == Vector([0, 2, 4])

def test_vector_addition_dimensionality_check():
    try:
        Vector([0, 1, 2]).add(Vector([0, 1, 2, 3]))
        assert False
    except ValueError:
        assert True

def test_vector_substraction():
    assert Vector([0, 1, 2]).substract(Vector([2, 1, 0])) == Vector([-2, 0, 2])

def test_vector_substraction_dimensionality_check():
    try:
        Vector([0, 1, 2]).substract(Vector([0, 1, 2, 3]))
        assert False
    except ValueError:
        assert True

def test_vector_dot_product():
    assert Vector([0, 1, 2]).dot(Vector([2, 1, 0])) == 1

def test_vector_magnitude():
    assert Vector([3, 4]).magnitude() == 5

def test_vector_euclidian_distance():
    assert Vector([3, 3, 3]).distance(Vector([2, 2, 2])) == 3 ** 0.5

def test_vector_cosine_similarity():
    assert Vector([3, 3, 3]).cosine_similarity(Vector([2, 2, 2])) == 18 / (27 ** 0.5 * 12 ** 0.5)

def test_vector_cosine_similarity_magnitude_check():
    try:
        Vector([0, 1, 2]).cosine_similarity(Vector([0, 0, 0]))
        assert False
    except ZeroDivisionError:
        assert True


if __name__ == '__main__':
    test_vector_creation()
    test_vector_type_check()
    test_vector_dimensionality_check()
    test_vector_scalars_check()
    test_vector_length()
    test_vector_3D_plot_error()
    test_scalar_multiplication()
    test_scalar_multiplication_type_check()
    test_vector_addition()
    test_vector_addition_dimensionality_check()
    test_vector_substraction()
    test_vector_substraction_dimensionality_check()
    test_vector_dot_product()
    test_vector_magnitude()
    test_vector_euclidian_distance()
    test_vector_cosine_similarity()
    test_vector_cosine_similarity_magnitude_check()

    print("All tests passed. ✅")
