from exceptions import InvalidProductNameError,InvalidPriceError,InvalidQuantityError

class Product:

    def __init__(self, product_id, name, category, price, quantity, minimum_stock_level):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.minimum_stock_level = minimum_stock_level

    @property
    def product_id(self):
        return self.__product_id
    @property
    def name(self):
        return self.__name
    @property
    def category(self):
        return self.__category
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    @property
    def minimum_stock_level(self):
        return self.__minimum_stock_level
    
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id
    
    @name.setter
    def name(self, name):
        name = name.strip()
        if not name:
            raise InvalidProductNameError("Product name cannot be empty.\n")
        self.__name = name
    
    @category.setter
    def category(self, category):
        self.__category = category
    
    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise InvalidPriceError("Price must be Numeric!!\n")
        if price <= 0:
            raise InvalidPriceError("Price must be greater than 0!!\n")
        self.__price = price
    
    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise InvalidQuantityError("Quantity must be an integer!!\n")
        if quantity < 0:
            raise InvalidQuantityError("Quantity cannot be negative!!\n")
        self.__quantity = quantity
    
    @minimum_stock_level.setter
    def minimum_stock_level(self, minimum_stock):
        if not isinstance(minimum_stock, int):
            raise InvalidQuantityError("Stock must be an integer!!\n")
        if minimum_stock < 0:
            raise InvalidQuantityError("Minimum stock level cannot be negative!!\n")
        self.__minimum_stock_level = minimum_stock

    def __str__(self):
        return f"Product Id        {self.product_id}\nName              :{self.name}\nCategory          :{self.category}\nPrice             :{self.price}\nQuantity          :{self.quantity}\nMinimum Stock     :{self.minimum_stock_level}\n"