"""Observer pattern task

Imagine a game where one or more rats can attack the player. Each rat individually has attack = 1. However,
the rats can form a swarm, and then the attack of each rat becomes equal to the number of all rats in the game.

The rat is added to the game by initializing the Rat object, and dies via the __exit__ method.

Implement the Game and Rat classes so that the attack value of the rats at any given time is correct and consistent.

An example of an API test you need to implement:

def test_three_rats_one_dies(self):
    game = Game()
    rat = Rat(game)
    self.assertEqual(1, rat.attack)
    rat2 = Rat(game)
    self.assertEqual(2, rat.attack)
    self.assertEqual(2, rat2.attack)
    with Rat(game) as rat3:
        self.assertEqual(3, rat.attack)
        self.assertEqual(3, rat2.attack)
        self.assertEqual(3, rat3.attack)
    self.assertEqual(2, rat.attack)
    self.assertEqual(2, rat2.attack)

Translated with www.DeepL.com/Translator (free version)
"""


"""
# *Start template
class Game:
    def __init__(self):
        pass
        # ToDo


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        # ToDo
"""


# ?Solution
class Game:
    def __init__(self):
        pass
        # ToDo


class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        # ToDo
