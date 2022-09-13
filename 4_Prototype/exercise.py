"""Task for pattern Prototype

Given class Point (point) and Line (line). Implement the deep_copy method to create a deep copy of the Line object.
This method must return a copy of the Line object with the start and end points copied.
Note: don't confuse deep_copy() with __deepcopy__()."""

import copy


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
        # ToDo
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
        new_start = Point(self.start.x, self.start.y)
        new_end = Point(self.end.x, self.end.y)
        return Line(new_start, new_end)


p = Line(start=Point(1, 2), end=Point(5, 6))
new_p = p.deep_copy()

new_p.start.x, new_p.start.y = 10, 20
new_p.end.x, new_p.end.y = 50, 60

print(p.start.x, p.start.y)
print(p.end.x, p.end.y)
print()
print(new_p.start.x, new_p.start.y)
print(new_p.end.x, new_p.end.y)
