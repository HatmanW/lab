

class Account:

    def __init__(self, name: str) -> None:
        '''
        This function is supposed to initialize the
        variables for account name (acct_name),
        and account balance (acct_Bal).
        :param name: name of account holder.
        '''
        self.__acct_name = name
        self.__acct_bal = 0


    def deposit(self, amount: float) -> bool:
        '''
        The point of this function is to deposit.
        If the amount entered is less than or equal to 0,
        nothing will happen.
        If the amount entered is a positive whole number,
        it will add the amount to the account balance.

        :param amount: This is the amount entered.
        :return: Result of calculation.
        '''
        if amount <=0:
            return False
        elif amount > 0:
            self.__acct_bal += amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        This Function is to withdraw.
        If the amount entered is less than or equal to 0,
        OR the amount is greater than the current account
        balance, nothing happens.
        If the amount is within our account balance range,
        it will subtract the ammount from our account balance

        :param amount: Amount to subtract from the account.
        :return: Result of calculation.
        '''
        if amount <= 0 or amount > self.__acct_bal:
            return False
        elif amount > 0:
            self.__acct_bal -= amount
            return True


    def get_balance(self) -> float:
        '''
        To get the current account balance.
        :return: Current account balance.
        '''
        return self.__acct_bal


    def get_name(self) -> str:
        '''
        To get the account name.
        :return: Current account name.
        '''
        return self.__acct_name