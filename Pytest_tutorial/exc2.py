'''

Prepare class Bank.
Class must have possibilites to withdraw and deposit money.
When class will be inicialized, bank must have 0 money.

Don't test case when you withdraw more than you can.


'''


class Bank:

    def __init__(self):
        self.amount = 0

    def deposit(self, value: int):
        self.value = value
        self.amount += value

    def withdraw(self, value: int):
        self.value = value
        self.amount -= value
        return value

