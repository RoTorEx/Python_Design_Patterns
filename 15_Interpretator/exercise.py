"""Interpreter pattern task

You need to implement a handler for simple numeric expressions with the following restrictions:

expressions use only numeric values (e.g., 12), variables consisting of only one character are added to expressions,
only addition and subtraction are supported from operations

there is no need to support brackets or any other operations

if the variable is not found in variables (or if you find a variable named with more than one character), the evaluator
should return zero

In case of any parsing errors, evaluator should return zero

Examples

calculate("1+2+3") = 6

calculate("1+2+xy")= 0

calculate("10-2-x") if x=3 is in variables = 5

Translated with www.DeepL.com/Translator (free version)"""


"""
# *Start template
class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        pass
        # ToDo
"""


# ?Solution
class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        pass
        # ToDo
