"""Decorator pattern task

You are given two types: Circle and Square. A ColoredShape decorator is also given.

The decorator adds a color to the string that describes the object of the particular shape.

However, there is room for a trick here:
the fact is that the decorator has a resize () method, which should change the size of the figure stored in it,
but at the same time, only the Circle class has a resize() method, while Square does not.

It is required to complete the proposed implementation pattern without adding the resize method to the Square class!

Here is an example of an API unit test that you need to implement.

class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual('A circle of radius 5 has the color red',
                         str(circle))
        circle.resize(2)
        self.assertEqual('A circle of radius 10 has the color red',
                         str(circle))"""


"""
# *Start template
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        pass
        # ToDo

class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        pass
        # ToDo


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        pass
        # ToDo
        # note that a Square doesn't have resize()

    def __str__(self):
        pass
        # ToDo
"""


# ?Solution
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        pass
        # ToDo


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        pass
        # ToDo


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        pass
        # ToDo
        # note that a Square doesn't have resize()

    def __str__(self):
        pass
        # ToDo
