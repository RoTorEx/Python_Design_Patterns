"""Proxy pattern task

Given a Person class. It is required to implement a ResponsiblePerson proxy class that:

does not allow Person to drink alcohol until the age of 18 (under 18 must return "too young")

does not allow Person to drive a car under 16 years old (up to 16 years old should return "too young")

in the case of drunk driving, regardless of age, returns 'dead'"""


"""
# *Start template
class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return "drinking"

    def drive(self):
        return "driving"

    def drink_and_drive(self):
        return "driving while drunk"


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    # ToDo
"""


# ?Solution
class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return "drinking"

    def drive(self):
        return "driving"

    def drink_and_drive(self):
        return "driving while drunk"


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person

    # ToDo
