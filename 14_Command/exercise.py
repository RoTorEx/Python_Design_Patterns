"""Command pattern task

Implement the Account.process() method to process various account-related commands.

The rules are simple:

    - the success flag indicates the success of the operation

    - to withdraw the amount of money, it must be in the account"""


from enum import Enum


"""
# *Start template
class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        pass
        # ToDo
"""


# ?Solution
class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True

        elif command.action == Command.Action.WITHDRAW:
            command.success = self.balance >= command.amount

            if command.success:
                self.balance -= command.amount


account = Account()
cmd_dp = Command(Command.Action.DEPOSIT, 6000)
cmd_wd = Command(Command.Action.WITHDRAW, 949)

print(account.balance)  # 0
account.process(cmd_dp)
print(account.balance)  # 6000
account.process(cmd_wd)
print(account.balance)  # 5051
