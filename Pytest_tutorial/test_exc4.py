from .exc4 import Bank, NotEnoughMoney
import pytest




class TestBank:

    def test_withdraw_over_amount(self):
        with pytest.raises(NotEnoughMoney):
            bank = Bank()
            bank.withdraw(200)
