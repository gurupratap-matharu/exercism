import sys
import threading
import unittest
import time

from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):
    """
    The main bank account testing class. Here we define various methods which specifically test our module for bugs and errors.
    """

    def setUp(self):
        self.account = BankAccount()

    def test_newly_opened_account_has_zero_balance(self):
        self.account.open()
        self.assertEqual(self.account.get_balance(), 0)

    def test_can_deposit_money(self):
        self.account.open()
        self.account.deposit(99)
        self.assertEqual(self.account.get_balance(), 99)

    def test_can_deposit_money_sequentially(self):
        self.account.open()
        self.account.deposit(20)
        self.account.deposit(30)

        self.assertEqual(self.account.get_balance(), 50)

    def test_can_withdraw_money(self):
        self.account.open()
        self.account.deposit(10)
        self.account.deposit(80)
        self.account.withdraw(30)
        self.account.withdraw(20)

        self.assertEqual(self.account.get_balance(), 40)

    def test_checking_balance_of_closed_account_throws_error(self):
        self.account.open()
        self.account.close()

        with self.assertRaises(ValueError):
            self.account.get_balance()


if __name__ == '__main__':
    unittest.main()
