""" Pattern task Builder

It is necessary to implement a template constructor to form pieces of code.
An example of using the API you need to support:

cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
print(cb)

Estimate exmaple output:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0

Dont forget about tabulation.

Example with empty class:

cb = CodeBuilder('Foo')
print(cb)
Estimate output:

class Foo:
  pass """


"""
# *Start template
class CodeBuilder:
    def __init__(self, root_name):
        # ToDo
        pass

    def add_field(self, type, name):
        # ToDo
        pass

    def __str__(self):
        # ToDo
        pass
"""


# ?Solution
class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.fields:
                lines.append('    %s' % f)
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()
