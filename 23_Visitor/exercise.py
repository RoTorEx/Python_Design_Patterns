"""Visitor pattern task

You need to implement an ExpressionPrinter to output various mathematical expressions. The expressions consist
of additions and multiplications.

Please put parentheses around addition operations, but not multiplication operations! Also remove whitespace
from the output.

Example:

Input: AdditionExpression(Value(2), Value(3))

Output: (2+3)

An example of an API test that you should support:

class Evaluate(unittest.TestCase):
    def test_simple_addition(self):
        simple = AdditionExpression(Value(2), Value(3))
        ep = ExpressionPrinter()
        ep.visit(simple)
        self.assertEqual("(2+3)", str(ep))

Taken from https://tavianator.com/the-visitor-pattern-in-python/
"""


import unittest
from abc import ABC


"""
# *Start Template
def _qualname(obj):
    "Get the fully-qualified name of an object (including module)."
    return obj.__module__ + "." + obj.__qualname__


def _declaring_class(obj):
    "Get the name of the class that declared an object."
    name = _qualname(obj)
    return name[: name.rfind(".")]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    "Actual visitor method implementation."
    key = (_qualname(type(self)), type(arg))
    if key not in _methods:
        raise Exception(f"Key {key} not found")
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    "Decorator that creates a visitor method."

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# ↑↑↑ LIBRARY CODE ↑↑↑


class Value:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        pass
        # ToDo :)

    def __str__(self):
        pass
        # ToDo
"""


# ?Solution
def _qualname(obj):
    "Get the fully-qualified name of an object (including module)."
    return obj.__module__ + "." + obj.__qualname__


def _declaring_class(obj):
    "Get the name of the class that declared an object."
    name = _qualname(obj)
    return name[: name.rfind(".")]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    "Actual visitor method implementation."
    key = (_qualname(type(self)), type(arg))
    if key not in _methods:
        raise Exception(f"Key {key} not found")
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    "Decorator that creates a visitor method."

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator


# ↑↑↑ LIBRARY CODE ↑↑↑


class Value:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        pass
        # ToDo :)

    def __str__(self):
        pass
        # ToDo
