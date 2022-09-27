"""Composite pattern task

Consider the code below. We have two classes SingleValue and ManyValues.
SingleValue stores a single numeric value, while ManyValues can store both numeric values and SingleValue objects.

You need to add a sum property to both SingleValue and ManyValues , which returns the sum of all the values stored in the object.
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

"""
# *Start template
class SingleValue:
    def __init__(self, value):
        self.value = value

class ManyValues(list):
    pass
"""


# ?Solution
class SingleValue:
    def __init__(self, value):
        self.value = value


class ManyValues(list):
    pass
