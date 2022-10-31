"""Task for the Snapshot pattern

The TokenMachine class must store tokens. Each Token is a reference object that holds a single numeric value.
The machine maintains the addition of tokens and when a token is added, the machine returns a memento (snapshot)
representing the state of the system at that point in time.

We need to fill in the gap by implementing the Memento pattern for this scenario. Carefully consider the scenario when
the token is passed from the outside as a reference, and then its internal value is changed from the outside. In such
a case, the machine must still return the correct system state!"""


from copy import deepcopy


"""
# *Start template
class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        pass
        # ToDo

    def revert(self, memento):
        pass
        # ToDo
"""


# ?Sulution
class Token:
    def __init__(self, value=0):
        self.value = value


class Memento(list):
    pass


class TokenMachine:
    def __init__(self):
        self.tokens = []

    def add_token_value(self, value):
        return self.add_token(Token(value))

    def add_token(self, token):
        self.tokens.append(token)
        return Memento(deepcopy(self.tokens))

    def revert(self, memento):
        self.tokens = [Token(x.value) for x in memento]
