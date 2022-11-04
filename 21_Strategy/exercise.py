"""Pattern Strategy task

Consider a quadratic equation and its canonical solution:

The part b^2-4*a*c is called the discriminant. Suppose we want to provide two APIs with different strategies for
calculating the discriminant.

In the OrdinaryDiscriminantStrategy , if the discriminant is < 0, we return it that way. This is normal, because the
main API returns a pair of complex numbers one way or another.

In the RealDiscriminantStrategy , if the discriminant is < 0, we have to return NaN (not a number). NaN goes through
the calculations, and the solver gives two NaN values. In Python, you can create such a number with float('nan').

Implement both strategies as well as the solver (solution algorithm). As for the pluses and minuses in the formula:
return the positive result with the first element and the negative with the second. Note that solve()
should return complex numbers!
"""


import cmath
import math
from abc import ABC


"""
# *Start Template
class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        pass
        # ToDo


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        pass
        # ToDo


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        "Returns a pair of complex (!) values."
        pass
        # ToDo
"""


# ?Solution
class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result = b * b - 4 * a * c
        return result if result >= 0 else float("nan")


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """Returns a pair of complex (!) values"""
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(disc)
        return ((-b + root_disc) / (2 * a), (-b - root_disc) / (2 * a))
