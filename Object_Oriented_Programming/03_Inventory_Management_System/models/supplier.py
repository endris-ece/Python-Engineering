from exceptions import InvalidNameError, InvalidPhoneNumberError, InvalidAddressError, InvalidEmailError

class Supplier:

    def __init__(self, supplier_id, first_name, last_name, phone, email, address):
        self.supplier_id = supplier_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.address = address
    
    @property
    def supplier_id(self):
        return self.__supplier_id

    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name

    @property
    def phone(self):
        return self.__phone
    
    @property
    def email(self):
        return self.__email

    @property
    def address(self):
        return self.__address

    
    @supplier_id.setter
    def supplier_id(self, supplier_id):
        self.__supplier_id = supplier_id
    
    @first_name.setter
    def first_name(self, first_name):
        if not first_name.isalpha():
            raise InvalidNameError("Name must only contain alphabets!!\n")
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, second_name):
        if not second_name.isalpha():
            raise InvalidNameError("Name must only contain alphabets!!\n")
        self.__last_name = second_name
    
    @phone.setter
    def phone(self, phone):
        if not (phone.isdigit() and len(phone) == 10 and phone.startswith("0")):
            raise InvalidPhoneNumberError("Phone number must only contain numerics and start with 0!!\n")
        self.__phone = f"+251 {phone[1:]}"

    @email.setter
    def email(self, email):
        if not ("@" in email and email.endswith(".com")):
            raise InvalidEmailError("Invalid Email. Email must contain '@' and ends with '.com'!!\n")
        self.__email = email
    
    @address.setter
    def address(self, address):
        for char in address:
            if not (char in [" ", "/", "."] or char.isalnum()):
                raise InvalidAddressError("Invalid address!!\n")
        self.__address = address
    
    def __str__(self):
        return f"Supplier ID :{self.supplier_id}\nName        :{self.first_name} {self.last_name}\nPhone       :{self.phone}\nEmail       :{self.email}\nAddress     :{self.address}\n"