from algebra.validator import LinearAlgebraValidator as linalgvalidator
from algebra.vectors import Vector

class Matrix:

    def __init__(self, data : list):
        """
        Create a Matrix object from a list of lists (rows of scalar values).

        Mathematical representation:
            A matrix is a rectangular array of numbers with dimensions (rows × columns),
            e.g., [[1, 2], [3, 4]] represents a 2×2 matrix.

        Parameters
        ----------
        data : list of lists
            The matrix data. Each element must be a list of scalar values (int or float),
            and all rows must have the same length.
        """

        # Validations
        linalgvalidator.validate_data_is_valid_matrix(data) 

        self.data = data
        self.dims = [len(data), len(data[0])]

    

    # OPERATIONS:
    def transpose(self):
        """
        Transpose the matrix (swap rows and columns).

        Returns
        -------
        Matrix
            A new Matrix object where rows become columns and columns become rows.

        Example
        -------
        Matrix([[1, 2],
                [3, 4]]).transpose()
        ➞ Matrix([[1, 3],
                [2, 4]])
        """

        # My implementation
        new_matrix = []
        for row_index, row in enumerate(self):
            for col_index, element in enumerate(row):
                if row_index == 0:
                    new_matrix.append([element])
                else:
                    new_matrix[col_index].append(element)
        
        return Matrix(new_matrix)
    
        # Optimized with zip -> transposed_data = [list(col) for col in zip(*self.data)]
    

    def add(self, other):
        """
        Add two matrices of the same dimensions, element-wise.

        Parameters
        ----------
        other : Matrix
            The matrix to add.

        Returns
        -------
        Matrix
            A new Matrix representing the sum.
        """

        linalgvalidator.validate_data_is_valid_matrix(other.data)
        linalgvalidator.validate_matrices_have_same_shape(self, other)

        new_matrix = [
            [a + b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self, other)
        ]

        return Matrix(new_matrix)
    
    
    def substract(self, other):
        """
        Substract two matrices of the same dimensions, element-wise.

        Parameters
        ----------
        other : Matrix
            The matrix to substract from self.

        Returns
        -------
        Matrix
            A new Matrix representing the difference.
        """

        linalgvalidator.validate_data_is_valid_matrix(other.data)
        linalgvalidator.validate_matrices_have_same_shape(self, other)

        new_matrix = [
            [a - b for a, b in zip(row_a, row_b)]
            for row_a, row_b in zip(self, other)
        ]

        return Matrix(new_matrix)
    
    
    def scalar_multiply(self, scalar):
        """
        Multiply the matrix by a scalar (element-wise multiplication).

        Mathematical definition:
            For a matrix A and scalar α,
            α * A = [[α ⋅ a₁₁, α ⋅ a₁₂, ..., α ⋅ a₁ₙ],
                    [α ⋅ a₂₁, α ⋅ a₂₂, ..., α ⋅ a₂ₙ],
                    ...
                    ]

        Parameters
        ----------
        scalar : int or float
            The scalar to multiply each element of the matrix with.

        Returns
        -------
        Matrix
            A new matrix with each element multiplied by the scalar.
        """

        linalgvalidator.validate_data_is_scalar(scalar)

        return Matrix([[a * scalar for a in row] for row in self])
    
    
    def dot(self, other):
        """
        Compute the matrix product (dot product) between two matrices.

        Mathematical definition:
            If A ∈ ℝᵐˣⁿ and B ∈ ℝⁿˣᵖ, then C = A ⋅ B ∈ ℝᵐˣᵖ where:
            C[i][j] = Σ (A[i][k] * B[k][j]) for k in [0, n)

        Parameters
        ----------
        other : Matrix
            The matrix to multiply with (on the right).

        Returns
        -------
        Matrix
            The resulting matrix product.
        """

        linalgvalidator.validate_data_is_valid_matrix(other.data)
        linalgvalidator.validate_matrices_are_compatible_for_matrix_product(self, other)

        
        row_vectors = [Vector(row) for row in self.data]
        col_vectors = [Vector(col) for col in other.transpose().data]
        
        new_matrix = [
            [row.dot(col) for col in col_vectors]
                for row in row_vectors
        ]
        
        return Matrix(new_matrix)
    
    
    def apply_to_vector(self, vector : Vector):
        """
        Apply the matrix as a linear transformation to a vector.

        Mathematical definition:
            If A ∈ ℝᵐˣⁿ and v ∈ ℝⁿ, then the transformation T(v) = A ⋅ v results in a new vector u ∈ ℝᵐ.

            This operation corresponds to applying the linear transformation represented by the matrix
            to the input vector, producing a new vector in the transformed space.

        Parameters
        ----------
        vector : Vector
            The vector to which the linear transformation (matrix) is applied.

        Returns
        -------
        Vector
            The resulting vector after applying the transformation.
        """

        linalgvalidator.validate_object_is_vector(vector)

        column_matrix = Matrix([[col] for col in vector.data])
        result_matrix = self.dot(column_matrix)
        transformed_vector = [row[0] for row in result_matrix.data]
        return Vector(transformed_vector)


    # OVERLOAD
    def __repr__(self):
        rows_str = ",\n        ".join(str(row) for row in self.data)
        return f"Matrix([\n        {rows_str}\n    ])"
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            return self.dot(other)
        elif isinstance(other, Vector):
            return self.apply_to_vector(other)
        else:
            raise TypeError(f"Unsupported operand type(s) for @: 'Matrix' and '{type(other).__name__}'")