""" Pattern task Factory
Given the class Man. It has two attributes: id and name .

Implement a PersonFactory with a raw create_person() method that takes a person's name and is instantiated
class Person with this name and id. The id field must start from zero.
That is, the factory will return the first instance with id = 0, the second one with id = 1, and so on."""


"""
# *Start template
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    def create_person(self, name):
        # todo
        pass
"""


# ?Solution
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


for name in ["Alex", "Sasha", "Valeriy", "Nikita"]:
    person = PersonFactory().create_person(f"{name}")
    print(person.id, person.name)
