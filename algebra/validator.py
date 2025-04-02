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

    @classmethod
    def _is_list_of_scalars(cls, data):
        return all(cls._is_scalar(x) for x in data)

    @classmethod
    def validate_data_is_list(cls, data):
        if not cls._is_list(data):
            raise TypeError("Expected a list as input.")

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

    @classmethod
    def validate_vector_is_in_2d(cls, x):
        if not cls._is_2d_vector(x):
            raise ValueError("Expected a 2D vector (list of length 2).")