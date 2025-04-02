import matplotlib.pyplot as plt
from algebra.vectors import Vector
from algebra.validator import LinearAlgebraValidator as validator

class LinearAlgebraVisualizer:

    @staticmethod
    def _plot_vectors(vectors, colors=None, labels=None, title=None, show=True):
        if colors is None:
            colors = ["blue"] * len(vectors)
        if labels is None:
            labels = [None] * len(vectors)

        for vec, color, label in zip(vectors, colors, labels):
            validator.validate_vector_is_in_2d(vec.data)
            plt.quiver(0, 0, vec.data[0], vec.data[1],
                       angles='xy', scale_units='xy', scale=1,
                       color=color, label=label)

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.grid()
        plt.gca().set_aspect('equal')

        if any(labels):
            plt.legend()
        if title:
            plt.title(title)
        if show:
            plt.show()

    @classmethod
    def plot_vector(cls, v: Vector):
        cls._plot_vectors([v], labels=["v"])

    @classmethod
    def plot_scalar_multiplication(cls, v: Vector, scalar):
        validator.validate_data_is_scalar(scalar)
        scaled = v.scalar_multiply(scalar)

        cls._plot_vectors(
            [v, scaled],
            colors=["blue", "red"],
            labels=["original", "scaled"],
            title=f"Scalar Multiplication: {scalar}"
        )
