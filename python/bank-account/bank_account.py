class BankAccount(object):
    def __init__(self):
        pass

    def get_balance(self):
        """Simply returns the balance of the account."""
        if self.balance DExists:
            return self.balance
        else:
            raise ValueError('Account ceases to exist.')

    def open(self):
        """
        We want to set the initial balance to zero upon account opening.
        """
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Deposit amount should be greater than zero!')
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError('Withdraw amount should be a positive number.')
        elif amount >= self.balance:
            print('Insufficient Funds!')
        else:
            self.balance -= amount

    def close(self):

        del self.balance
        print('Account closed')


if __name__ == '__main__':

    b1 = BankAccount()
    b1.open()
    print(b1.get_balance())
    b1.deposit(99)
    print(b1.get_balance())
    b1.withdraw(11)
    print(b1.get_balance())
    b1.close()
    print(b1.get_balance())
