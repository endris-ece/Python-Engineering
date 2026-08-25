from exceptions import InvalidQuantityError

class Transaction:

    def __init__(self, transaction_id, product_id, supplier_id, transaction_type, quantity, date):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.date = date

    @property
    def transaction_id(self):
        return self.__transaction_id
    
    @property
    def product_id(self):
        return self.__product_id

    @property
    def supplier_id(self):
        return self.__supplier_id

    @property
    def transaction_type(self):
        return self.__transaction_type
    
    @property
    def quantity(self):
        return self.__quantity

    @property
    def date(self):
        return self.__date

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id
    
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id
    
    @supplier_id.setter
    def supplier_id(self, supplier_id):
        self.__supplier_id = supplier_id

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type
    
    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise InvalidQuantityError("Quantity must be an integer!!\n")
        if int(quantity) <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0!!\n")
        self.__quantity =quantity

    @date.setter
    def date(self, date):
        self.__date = date

    def __str__(self):
        return f"Transaction ID     :{self.transaction_id}\nProduct ID         :{self.product_id}\nTransaction Type   :{self.transaction_type}\nQuantity           :{self.quantity}\nDate               :{self.date}\n"