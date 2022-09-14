"""Task for pattern Adapter

You are given a Square class and a calculate_area() function that calculates the area of a rectangle.
To be able to pass an instance of the Square class to the calculate_area() method,
you need to implement the SquareToRectangleAdapter class.
This adapter takes an instance of a square and adapts it so that an instance of this adapter
can be passed to the calculate_area() method."""


"""
# *Start template
class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        # ToDo
"""


# ?Solution
class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        # ToDo
        pass
