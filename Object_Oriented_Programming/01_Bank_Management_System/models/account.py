from exceptions import InvalidBalanceError, InvalidAccountTypeError
from enum import Enum

class AccountType(Enum):
    SAVINGS = "Savings"
    BUSINESS = "Business"

class Account:

    def __init__(self, account_number, customer, balance, account_type):
        self.account_number = account_number
        self.customer = customer
        self.balance = balance
        self.account_type = account_type


    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def account_type(self):
        return self.__account_type

    @property
    def balance(self):
        return self.__balance

    @customer.setter
    def customer(self, customer):
        self._customer = customer

    @account_number.setter
    def account_number(self, acc_number):
        self.__account_number = acc_number

    @account_type.setter
    def account_type(self, acc_type):
        if not (acc_type.title() == AccountType.SAVINGS.value or acc_type.title() == AccountType.BUSINESS.value):
            raise InvalidAccountTypeError(acc_type)
        self.__account_type = acc_type

    @balance.setter
    def balance(self, balance):
        if not isinstance(balance, (int, float)):
            raise InvalidBalanceError(balance)
        if int(balance) < 0:
            raise InvalidBalanceError(balance)
        self.__balance = balance

    def __str__(self):
        return f"Account Number  :  {self.__account_number}\nBalance         :  {self.balance}\nType            :  {self.__account_type}\nOwner           :  {self._customer}"
