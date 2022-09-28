"""Composite pattern task

Consider the code below. We have two classes SingleValue and ManyValues.
SingleValue stores a single numeric value, while ManyValues can store both numeric values and SingleValue objects.

You need to add a sum property to both SingleValue and ManyValues , which returns the sum of all the values
stored in the object.
In this case, you need to implement the only property sum! That is, you should not add sum physically to both classes.

Here is an example of a unit test code that you should come up with:

class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)

        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)

        self.assertEqual(all_values.sum, 66)"""


from abc import ABC
from collections.abc import Iterable


"""
# *Start template
class SingleValue:
    def __init__(self, value):
        self.value = value

class ManyValues(list):
    pass
"""


# ?Solution
class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            print(c)
            for i in c:
                result += i
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass


multiple = ManyValues()
multiple.append(1)
multiple.append(2)
multiple.append(3)
multiple.append(6)

single = SingleValue(12)

all_values = ManyValues()
all_values.append(multiple)
all_values.append(single)

values_sum = all_values.sum
print(values_sum)  # 24
