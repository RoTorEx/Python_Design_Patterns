"""Chain of Responsibility pattern task

Given a game project with the classes Goblin and GoblinKing. Implement the following rules:

Goblin has base stats 1 attack / 1 defense (1/1), goblin king has 3/3

When goblin king is in play, all other goblins get +1 attack

Goblins get +1 defense for every other goblin in the game (the goblin king is also a goblin!)

For example:

There are 3 goblins in the game. Then each has the following characteristics - 1/3 (1/1 base + 0/2 defense bonus)

Goblin king comes into the game.
Now the characteristics of each goblin are 2/4 (
    1/1 + 0/3 bonus to defense against "goblin friends"+ 1/0 to attack from goblin king
)

The state of all goblins at any given time must be consistent.
"""

from abc import ABC
from enum import Enum

"""
# *Start template
class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        # ToDo
        pass


class GoblinKing(Goblin):
    def __init__(self, game):
        # ToDo
        pass


class Game:
    def __init__(self):
        self.creatures = []
"""


# ?Solution
class Creature(ABC):
    def __init__(self, game, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game

    @property
    def attack(self):
        pass

    @property
    def defense(self):
        pass

    def query(self, source, query):
        pass


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    @property
    def attack(self):
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)

    def query(self, source, query):
        if self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)


class Query:
    def __init__(self, initial_value, what_to_query):
        self.what_to_query = what_to_query
        self.value = initial_value


class Game:
    def __init__(self):
        self.creatures = []
