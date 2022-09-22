from exception import AccountWithdrawalException


class Account:
    balance = 0

    def __init__(self, name):
        self.name = name

    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount: float):
        if amount > self.balance or amount < 0:
            raise AccountWithdrawalException("Amount shouldn't be negative value")

        self.balance -= amount








