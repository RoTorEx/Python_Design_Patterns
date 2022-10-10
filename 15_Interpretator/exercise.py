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


import re
from enum import Enum


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
def megasplit(pattern, string):
    splits = list((m.start(), m.end()) for m in re.finditer(pattern, string))
    starts = [0] + [i[1] for i in splits]
    ends = [i[0] for i in splits] + [len(string)]
    return [string[start:end] for start, end in zip(starts, ends)]


class ExpressionProcessor:
    class NextOp(Enum):
        PLUS = 1
        MINUS = 2

    def __init__(self):
        self.variables = {}

    def calculate(self, expression):
        current = 0
        next_op = None

        # doesn't work in python 3.5
        # parts = re.split('(?<=[+-])', expression)
        parts = megasplit("(?<=[+-])", expression)

        for part in parts:
            noop = re.split("[\+\-]", part)
            first = noop[0]
            value = 0

            try:
                value = int(first)
            except ValueError:
                if len(first) == 1 and first[0] in self.variables:
                    value = self.variables[first[0]]
                else:
                    return 0

            if not next_op:
                current = value
            elif next_op == self.NextOp.PLUS:
                current += value
            elif next_op == self.NextOp.MINUS:
                current -= value

            if part.endswith("+"):
                next_op = self.NextOp.PLUS
            elif part.endswith("-"):
                next_op = self.NextOp.MINUS

        return current
