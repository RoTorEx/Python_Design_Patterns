"""Open / Closed Principle (OCP)."""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    """By adding another class method, we violate the open/closed rule.
      That is, the class is closed for sharing and can only be modified.
      Classes should be closed to modifications."""

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # state space explosion
    # 3 criteria
    # c s w cs sw cw csw = 7 methods

    # ?OCP = open for extension, closed for modification.For new methods we should use to mofificate class


# *Corparative template
class Specification:
    """Determines whether a particular element will satisfy a certain criterion.
    We wiil be modificate this class in future."""
    def is_satisfied(self, item):
        pass

    # Here we use operator overload (&) and operator makes life easier
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    """We wiil be modificate this class in future."""
    def filter(self, items, spec):
        pass


# Filtration by color
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


# Filter by size
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# Combinator
# class AndSpecification(Specification):
#     def __init__(self, spec1, spec2):
#         self.spec2 = spec2
#         self.spec1 = spec1
#
#     def is_satisfied(self, item):
#         return self.spec1.is_satisfied(item) and \
#                self.spec2.is_satisfied(item)


# Very good compinator!
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print("Green products (old):")
for p in pf.filter_by_color(products, Color.GREEN):
    print(f" - {p.name} is green")
# ^ BEFORE

# v AFTER
bf = BetterFilter()

print("Green products (new):")
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f" - {p.name} is green")

print("Large products:")
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f" - {p.name} is large")

print("Large blue items:")
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue = large & ColorSpecification(Color.BLUE)  # & will unite this two specification using overload operator
for p in bf.filter(products, large_blue):
    print(f" - {p.name} is large and blue")
