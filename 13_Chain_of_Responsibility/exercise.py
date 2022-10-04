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
class Creature:
    ...


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
