""" Задача на паттерн Фабрика
Дан класс Person. У него есть два атрибута: id и name .

Реализуйте PersonFactory с не статическим методом create_person(), который принимает имя человека и возвращет экземпляр
класс Person с этим именем и id. Поле id должно начинаться с нуля.
То есть, фабрика вернёт первый экземпляр с id = 0, второй с id = 1 и так далее."""


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
    def create_person(self, name):
        # todo
        pass
