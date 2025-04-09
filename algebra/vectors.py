from algebra.validator import LinearAlgebraValidator as linalgvalidator

class Vector():

    def __init__(self, data : list):

        
        # --- Validations ---
        linalgvalidator.validate_data_is_list(data)
        linalgvalidator.validate_data_only_contains_scalars(data)

        self.data = data
        self.length = len(data)
    
    def __repr__(self):
        return f"Vector({self.data})"
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.data == other.data


    
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
        linalgvalidator.validate_data_is_scalar(scalar)


        return Vector([scalar * value for value in self.data])
    
    
    def add(self, vector2 : "Vector"):
        """
        Add two vectors of the same dimension.

        Mathematical definition:
            For vectors v = [v₁, ..., vₙ] and w = [w₁, ..., wₙ],
            the sum is v + w = [v₁ + w₁, ..., vₙ + wₙ]

        Parameters
        ----------
        vector2 : Vector
            The vector to add to self.

        Returns
        -------
        Vector
            A new vector representing the sum.
        """

        # --- Validations ---
        linalgvalidator.validate_data_is_vector(vector2)
        linalgvalidator.validate_vectors_have_same_size(self, vector2)

        return Vector([a + b for a, b in zip(self.data, vector2.data)])
    
    
    def substract(self, vector2 : "Vector"):
        """
        Substract another vector from this one.

        Mathematical definition:
            For vectors v = [v₁, ..., vₙ] and w = [w₁, ..., wₙ],
            the difference is v - w = [v₁ - w₁, ..., vₙ - wₙ]

        Parameters
        ----------
        vector2 : Vector
            The vector to substract from self.

        Returns
        -------
        Vector
            A new vector representing the difference.
        """

        # --- Validations ---
        linalgvalidator.validate_data_is_vector(vector2)
        linalgvalidator.validate_vectors_have_same_size(self, vector2)

        return Vector([a - b for a, b in zip(self.data, vector2.data)])
    
    
    def dot(self, vector2: "Vector"):
        """
        Compute the dot product between two vectors of the same dimension, the sum of the products of every corresponding components.

        Mathematical definition:
            v · w = Σ (vᵢ * wᵢ), for i in [1, n]

        Parameters
        ----------
        vector2 : Vector
            The second vector in the dot product.

        Returns
        -------
        float
            The scalar result of the dot product.
        """

        # --- Validations ---
        linalgvalidator.validate_data_is_vector(vector2)
        linalgvalidator.validate_vectors_have_same_size(self, vector2)

        
        dot_product = sum(a * b for a, b in zip(self.data, vector2.data))
        return dot_product

    
    def magnitude(self):
        """
        Compute the magnitude (Euclidean norm) of the vector.

        Mathematical definition:
            ||v|| = sqrt(v · v) = sqrt(Σ vᵢ²)

        Returns
        -------
        float
            The Euclidean norm of the vector.
        """

        magnitude = sum(a**2 for a in self.data) ** 0.5
        return magnitude
    
    
    def distance(self, vector2: "Vector"):
        """
        Compute the Euclidean distance between two vectors.

        Mathematical definition:
            d(v, w) = ||v - w|| = sqrt(Σ (vᵢ - wᵢ)²)

        Parameters
        ----------
        vector2 : Vector
            The second vector to compute the distance from.

        Returns
        -------
        float
            The Euclidean distance between the two vectors.
        """

        # --- Validations ---
        linalgvalidator.validate_data_is_vector(vector2)
        linalgvalidator.validate_vectors_have_same_size(self, vector2)

        
        distance = self.substract(vector2).magnitude()
        return distance
    
    
    def cosine_similarity(self, vector2: "Vector"):
        """
        Compute the cosine similarity between two vectors.

        Mathematical definition:
            cos(θ) = (v · w) / (||v|| * ||w||)

        Parameters
        ----------
        vector2 : Vector
            The second vector to compare with.

        Returns
        -------
        float
            A scalar between -1 and 1 representing the cosine similarity.
        """

        # --- Validations ---
        linalgvalidator.validate_data_is_vector(vector2)
        linalgvalidator.validate_vectors_have_same_size(self, vector2)
        linalgvalidator.validate_vector_has_non_null_magnitude(self)
        linalgvalidator.validate_vector_has_non_null_magnitude(vector2)

        
        cosine = self.dot(vector2) / (self.magnitude() * vector2.magnitude())
        return cosine



    # OVERLOAD
    def __repr__(self):
        return f"Vector({self.data})"
    
    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.substract(other)
    
    def __mul__(self, other):
        linalgvalidator.validate_data_is_scalar(other)
        return self.scalar_multiply(other)

    def __rmul__(self, other):
        return self.__mul__(other)




        


