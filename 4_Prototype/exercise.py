""" Task for pattern Prototype
Given class Point (point) and Line (line). Implement the deep_copy method to create a deep copy of the Line object.

This method must return a copy of the Line object with the start and end points copied.

Note: don't confuse deep_copy() with __deepcopy__() """


"""
# *Start template
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        # ToDO
"""


# ?Solution
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        pass
        # ToDO
