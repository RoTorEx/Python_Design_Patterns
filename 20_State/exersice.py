"""State pattern task

A combination lock is a lock that opens after entering the correct sequence of numbers.
The lock is programmed for a combination (say, 12345) and then the user is expected to enter that exact sequence to open the lock.

The lock has a Status, which reflects the current state of the lock.

The rules are as follows:

If the lock has just been closed (or if we are talking about the initial state) - the status should be LOCKED

The sequence of entered digits should be displayed in the status

If the user entered the right sequence, the lock status should change to OPEN

If user enters wrong sequence, lock status should change to ERROR

Please implement CombinationLock.

An example of test API you need to implement

class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)

Translated with www.DeepL.com/Translator (free version)
"""


"""
# *Start template
class CombinationLock:
    def __init__(self, combination):
        self.status = "LOCKED"
        # ToDo

    def reset(self):
        pass
        # ToDo - reset lock to LOCKED state

    def enter_digit(self, digit):
        pass
        # ToDo
"""


# ?Solution
class CombinationLock:
    def __init__(self, combination):
        self.status = "LOCKED"
        # ToDo

    def reset(self):
        pass
        # ToDo - reset lock to LOCKED state

    def enter_digit(self, digit):
        pass
        # ToDo
