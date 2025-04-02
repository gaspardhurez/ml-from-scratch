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
    assert Vector([0, 1, 2]).scalar_multiply(5).data == Vector([0, 5, 10]).data

def test_scalar_multiplication_type_check():
    try:
        Vector([0, 1, 2]).scalar_multiply("10")
        assert False
    except TypeError:
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


    print("All tests passed. ✅")
