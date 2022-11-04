"""Template Method pattern task

Imagine a typical collectible card game in which cards represent creatures.
Each creature has two attributes: attack and health. Creatures can fight by dealing damage equal to their attack value
(reducing the health of the creature being attacked).

The CardGame class implements the logic for two fighting creatures. However, the exact mechanics of dealing damage
may vary:

TemporaryCardDamage : in some games (e.g. Magic: the Gathering), until a creature is destroyed, its health is restored
to its original level at the end of each combat.

PermanentCardDamage : in other games (e.g. Hearthstone), the damage dealt is saved.

Implement classesTemporaryCardDamageGame and PermanentCardDamageGame that implement the described logic.

A couple of examples:

In temporary damage mode, two creatures with characteristics 1/2 and 1/3 can never kill each other.
In permanent damage mode, the second creature wins in two rounds.

In either of the two modes, two creatures with characteristics 2/2 will kill each other."""


from abc import ABC


"""
# *Start Template
class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        pass
        # ToDo

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    pass
    # ToDo


class PermanentDamageCardGame(CardGame):
    pass
    # ToDo
"""


# ?Solution
class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        first = self.creatures[c1_index]
        second = self.creatures[c2_index]
        self.hit(first, second)
        self.hit(second, first)
        first_alive = first.health > 0
        second_alive = second.health > 0
        if first_alive == second_alive:
            return -1
        return c1_index if first_alive else c2_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        old_health = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = old_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
