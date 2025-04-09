
class LinearAlgebraValidator:

    # --------------------
    # DATA TYPES
    # --------------------

    @staticmethod
    def _is_scalar(x):
        return isinstance(x, (int, float)) and not isinstance(x, bool)

    @staticmethod
    def _is_list(x):
        return isinstance(x, list)
    
    @staticmethod
    def _is_vector(x):
        return x.__class__.__name__ == "Vector"

    @classmethod
    def _is_list_of_scalars(cls, data):
        return all(cls._is_scalar(x) for x in data)

    @classmethod
    def validate_data_is_list(cls, data):
        if not cls._is_list(data):
            raise TypeError("Expected a list as input.")
    
    @classmethod
    def validate_data_is_vector(cls, data):
        if not cls._is_vector(data):
            raise TypeError("Expected a Vector object as input.")

    @classmethod
    def validate_data_is_scalar(cls, data):
        if not cls._is_scalar(data):
            raise TypeError("Expected a scalar value (non-boolean int or float).")

    @classmethod
    def validate_data_only_contains_scalars(cls, data):
        if not cls._is_list_of_scalars(data):
            raise TypeError("List must contain only scalar values (int or float, excluding bool).")


    # --------------------
    # DIMENSIONALITY
    # --------------------

    @staticmethod
    def _is_2d_vector(x):
        return len(x) == 2
    
    @staticmethod
    def _are_same_sized_vectors(x1, x2):
        return len(x1.data) == len(x2.data)
    
    @staticmethod
    def _are_same_shape_matrices(X1, X2):
        return X1.dims == X2.dims
    
    @staticmethod
    def _are_same_sized_rows(rows_list):
        row_lengths = [len(row) for row in rows_list]
        return len(set(row_lengths)) == 1
         

    @classmethod
    def validate_vector_is_in_2d(cls, x):
        if not cls._is_2d_vector(x):
            raise ValueError("Expected a 2D vector (list of length 2).")
    
    @classmethod
    def validate_vectors_have_same_size(cls, x1, x2):
        if not cls._are_same_sized_vectors(x1, x2):
            raise ValueError("Vectors are not the same dimension.")
    
    @classmethod
    def validate_matrices_have_same_shape(cls, x1, x2):
        if not cls._are_same_shape_matrices(x1, x2):
            raise ValueError("Matrices are not the same shape.")
    
    
    # --------------------
    # VECTORS & MATRICES
    # --------------------

    @classmethod
    def validate_data_is_valid_matrix(cls, data):
        
        if not cls._is_list(data):
            raise TypeError("Expected a list as input.")
        
        for row in data:
            if not cls._is_list(row):
                raise TypeError("Each row must be a list.")
            if not cls._is_list_of_scalars(row):
                raise TypeError("Each row must only contain scalar values.")
        
        if not cls._are_same_sized_rows(data):
            raise ValueError("Matrix rows must all be the same length.")

    # --------------------
    # VECTOR OPERATIONS
    # --------------------

    @staticmethod
    def _has_non_null_magnitude(x):
        return x.magnitude() != 0
    
    @classmethod
    def validate_vector_has_non_null_magnitude(cls, x):
        if not cls._has_non_null_magnitude(x):
            raise ZeroDivisionError("Cannot compute cosine similarity with a zero vector.")
    
    
