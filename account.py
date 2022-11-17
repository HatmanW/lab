

class Account:

    def __init__(self, name):

        self.acct_name = name
        self.acct_bal = 0


    def deposit(self, amount):

        if amount <=0:
            return False
        self.acct_bal += amount
        return True

    def withdraw(self, amount):

        if amount <= 0 or amount > self.acct_bal:
            return False
        self.acct_bal -= amount
        return True


    def get_balance(self):

        return self.acct_bal


    def get_name(self):

        return self.acct_name