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

    @property
    def age(self):
        return self.person.age

    @age.setter
    def age(self, value):
        self.person.age = value

    def drink(self):
        if self.age >= 18:
            return self.person.drink()
        return "Too young!"

    def drive(self):
        if self.age >= 16:
            return self.person.drive()
        return "To young!"

    def drink_and_drive(self):
        return "Dead..."


person = Person(18)
print(f"{18} years old:\n{person.drink()} <> {person.drive()} <> {person.drink_and_drive()}")

for age in [10, 17, 15, 22, 40]:
    person = Person(age)
    res_person = ResponsiblePerson(person)

    print(f"{age} years old:\n{res_person.drink()} <> {res_person.drive()} <> {res_person.drink_and_drive()}\n")
