import unittest

from account import Account
from exception import AccountWithdrawalException


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.acc = Account("Elder Jega")

    def test_account_can_be_created(self):
        self.assertIsNotNone(self.acc)

    def test_that_account_has_zero_balance_on_creation(self):
        self.assertEqual(0, self.acc.get_balance())

    def test_that_account_has_a_name(self):
        self.assertEqual("Elder Jega", self.acc.name)

    def test_that_account_can_deposit(self):
        self.acc.deposit(5000)
        self.assertEqual(5000, self.acc.get_balance())

    def test_that_account_can_withdraw(self):
        self.acc.deposit(3000)
        self.assertEqual(3000, self.acc.get_balance())
        self.acc.withdraw(2000)
        self.assertEqual(1000, self.acc.get_balance())

    def test_that_amount_greater_than_balance_cannot_be_withdraw(self):
        self.acc.deposit(1000)
        self.assertEqual(1000, self.acc.get_balance())
        with self.assertRaises(AccountWithdrawalException):
            self.acc.withdraw(3000)

    def test_that_negative_amount_cannot_be_withdrawn(self):
        with self.assertRaises(AccountWithdrawalException):
            self.acc.withdraw(-1000)


if __name__ == '__main__':
    unittest.main()
