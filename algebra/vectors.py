from algebra.validator import LinearAlgebraValidator as validator

class Vector():

    def __init__(self, data : list):

        
        # --- Validations ---
        validator.validate_data_is_list(data)
        validator.validate_data_only_contains_scalars(data)

        self.data = data
        self.length = len(data)
    
    def __repr__(self):
        return f"Vector({self.data})"
    
    
    # VECTOR OPERATIONS
    def scalar_multiply(self, scalar):
        """
        Multiply the vector by a scalar.
        Mathematical definition:
            For a vector v = [v₁, v₂, ..., vₙ] and scalar α, the scalar product is α * v = [α⋅v₁, α⋅v₂, ..., α⋅vₙ]
        This operation is one of the two axioms of linearity (homogeneity).
        
        Parameters
        ----------
        scalar : int or float
            The scalar value to multiply with the vector.

        Returns
        -------
        Vector
            A new vector resulting from the multiplication.
        """

        # --- Validations ---
        validator.validate_data_is_scalar(scalar)


        return Vector([scalar * value for value in self.data])



        


