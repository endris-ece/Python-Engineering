class InvalidPhoneError(Exception):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        super().__init__(
            f"Phone number '{phone_number}' is invalid. "
            f"It must be exactly 10 numeric digits long and start with 0."
        )
        
class InvalidNameError(Exception):
    def __init__(self, name):
        self.name = name

        super().__init__(
            f"{name} contains non-alphabetic characters. "
            f"Input must contain only alphabets!"
            )

class InvalidEmailError(Exception):
    def __init__(self, email):
        super().__init__(
            f"Email '{email}' is invalid.\nIt must contain the '@' symbol."
        )


class InvalidAccountTypeError(Exception):
    def __init__(self, acc_type):
        super().__init__(
            f"Account type must be 'BUSINESS' or 'SAVINGS'"
        )
class InvalidBalanceError(Exception):
    def __init__(self, balance):
        self.balance = balance

        super().__init__(
            f"Invalid balance {balance}"
            f"Balance should be a positive numeric value."
            )

