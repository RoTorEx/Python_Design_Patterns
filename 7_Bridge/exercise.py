"""Bridge pattern task

You are given an inheritance hierarchy, the problem of which is the need to implement a huge number of classes.
We need to refactor this hierarchy by defining a constructor in the Shape base class that accepts a Renderer interface, declared as:

class Renderer(ABC):

    @property

    def what_to_render_as(self):

        return None

VectorRenderer and RasterRenderer must also operate through the Renderer interface.
Each Shape class descendant must have a constructor that accepts a Renderer
and is implemented in such a way that calls to __str__() on instances of those descendants must work correctly.

For example:

str(Triangle(RasterRenderer()) # returns 'Drawing Triangle as pixels'"""

from abc import ABC


"""
# *Start template
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# ToDo: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
"""


# ?Solution
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None

# ToDo: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer
