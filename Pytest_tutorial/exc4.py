'''

Continue exc2 and change section with withdrawal more money than it's deposite in bank - add error

'''


class NotEnoughMoney(Exception):
    pass


class Bank:

    def __init__(self):
        self.amount = 0

    def deposit(self, value: int):
        self.value = value
        self.amount += value

    def withdraw(self, value: int):
        if value > self.amount:
            raise NotEnoughMoney('I haven\'t got enough money')

        self.value = value
        self.amount -= value
        return value