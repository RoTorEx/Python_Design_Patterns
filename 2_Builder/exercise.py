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
        # todo
        pass

    def add_field(self, type, name):
        # todo
        pass

    def __str__(self):
        # todo
        pass
"""


# ?Solution
class CodeBuilder:
    def __init__(self, root_name):
        # todo
        pass

    def add_field(self, type, name):
        # todo
        pass

    def __str__(self):
        # todo
        pass
