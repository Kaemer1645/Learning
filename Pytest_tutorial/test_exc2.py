from .exc2 import Bank

class TestBank:

    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)


    def test_deposit(self):
        #given
        bank = Bank()

        #when
        bank.deposit(100)

        #then
        assert bank.amount == 100

    def test_deposit_twice(self):
        #given
        bank = Bank()

        #when
        bank.deposit(100)
        bank.deposit(100)

        #then
        assert bank.amount == 200

    def test_withdraw(self):
        #given
        bank = Bank()
        bank.deposit(100)
        #when
        withdraw = bank.withdraw(100)

        #then
        assert withdraw == 100
        assert bank.amount == 0
