from algebra.matrices import Matrix
from algebra.vectors import Vector
from algebra.validator import LinearAlgebraValidator as linalgvalidtor

class AugmentedMatrix(Matrix):

    def __init__(self, A: Matrix, b: Vector):
        """
        Create an augmented matrix [A | b] from a matrix A and a vector b.

        This constructor validates that A is a valid matrix and b is a valid vector,
        and ensures that the number of rows in A matches the number of elements in b.
        It then appends each element of b as an additional column to the corresponding
        row of A, forming the augmented matrix used in solving systems of linear equations.

        Parameters
        ----------
        A : Matrix
            The coefficient matrix of the linear system (size m × n).
        b : Vector
            The right-hand side vector (size m).
        """

        linalgvalidtor.validate_object_is_matrix(A)
        linalgvalidtor.validate_object_is_vector(b)
        linalgvalidtor.validate_matrix_and_vector_have_same_length(A, b)
        augmented_matrix = [row + [b.data[i]] for i, row in enumerate(A.data)]
        super().__init__(augmented_matrix)
        self.original_matrix = A
        self.original_vector = b