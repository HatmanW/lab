
from pytest import *
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Jane')

    def tearDown(self):
        del self.a1
        del self.a2


    def test_init_(self):
        assert self.a1.get_name() =='John'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'Jane'
        assert self.a2.get_balance() == 0


    def test_deposit(self):
        assert self.a1.deposit(-2) == False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(2) == True
        assert self.a1.get_balance() == 2
        assert self.a1.deposit(0) == False
        assert self.a1.get_balance() == 2

        assert self.a1.deposit(6.3) == True
        assert self.a1.get_balance() == approx(8.3, abs = 0.001)

        assert self.a2.deposit(-2) == False
        assert self.a2.get_balance() == 0
        assert self.a2.deposit(5) == True
        assert self.a2.get_balance() == 5
        assert self.a2.deposit(0) == False
        assert self.a2.get_balance() == 5

        assert self.a2.deposit(4.5) == True
        assert self.a2.get_balance() == approx(9.5, abs= 0.001)


    def test_withdraw(self):
        assert self.a1.withdraw(-2) == False
        assert self.a1.get_balance() == 0
        self.a1.deposit(5)
        assert self.a1.withdraw(2) == True
        assert self.a1.get_balance() == 3
        assert self.a1.withdraw(0) == False
        assert self.a1.get_balance() == 3

        assert self.a1.withdraw(2.0) == True
        assert self.a1.get_balance() == approx(1.0, abs =0.001)

        assert self.a2.withdraw(-2) == False
        assert self.a2.get_balance() == 0
        self.a2.deposit(6)
        assert self.a2.withdraw(3) == True
        assert self.a2.get_balance() == 3
        assert self.a2.withdraw(0) == False
        assert self.a2.get_balance() == 3

        assert self.a2.withdraw(2.0) == True
        assert self.a2.get_balance() == approx(1.0, abs =0.001)

