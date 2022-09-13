import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("123 London Road", "London", "UK"))
print(john)

# !Broken way
# jane = john
# jane.name = "Jane"

# ?Best way to make new object using old prototype
jane = copy.deepcopy(john)  # Copy all info, include Address
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print(john, jane, sep="\n")
