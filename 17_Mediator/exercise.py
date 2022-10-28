"""Mediator pattern task

There can be any number of instances of the Participant class in the system.
Each instance has an integer value attribute initially initialized to zero.

The participant instance can say say() by emitting a value, broadcasting it to all participants.
At a given point in time, each participant is required to increase its own value by the translated value.

Example

The two participants start with value 0 respectively

Participant 1 broadcasts value 3. Now we have Participant 1 value = 0, Participant 2 value = 3

Participant 2 broadcasts value 2. Now we have Participant 1 value = 2, Participant 2 value = 3"""


"""
# *Start template
class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator

    def say(self, value):
        pass
        # ToDo
"""


# ?Solution
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.alert.append(self.mediator_alert)

    def mediator_alert(self, sender, value):
        if sender != self:
            self.value += value

    def say(self, value):
        self.mediator.broadcast(self, value)


class Mediator:
    def __init__(self):
        self.alert = Event()

    def broadcast(self, sender, value):
        self.alert(sender, value)
