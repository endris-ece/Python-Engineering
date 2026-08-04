from exceptions import InvalidPhoneError, InvalidNameError, InvalidEmailError

class Customer:

    def __init__(self, c_ID, f_name, s_name, phone, email, address):
        self.f_name = f_name
        self.s_name = s_name
        self.phone = phone
        self.c_ID = c_ID
        self.email = email
        self.address = address

    @property
    def c_ID(self):
        return self.__c_ID

    @property
    def f_name(self):
        return self.__f_name

    @property
    def s_name(self):
        return self.__s_name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email
    @property
    def address(self):
        return self.__address

    @f_name.setter
    def f_name(self, name):
        if not name.isalpha():
            raise InvalidNameError(name)
        self.__f_name = name

    @s_name.setter
    def s_name(self, name):
        if not name.isalpha():
            raise InvalidNameError(name)
        self.__s_name = name

    @phone.setter
    def phone(self, phone):
        if not phone.isdigit() or len(phone) != 10 or not phone.startswith("0"):
            raise InvalidPhoneError(phone)
        self.__phone = f"+251 {phone[1:]}"

    @email.setter
    def email(self, email):
        if "@" not in email:
            raise InvalidEmailError(email)
        self.__email = email

    @address.setter
    def address(self, address):
        self.__address = address
    
    @c_ID.setter
    def c_ID(self, c_ID):
        self.__c_ID = c_ID

    def __str__(self):
        return f"Full name       :  {self.__f_name} {self.__s_name}\nCustomer ID     :  {self.__c_ID}\nPhone           :  {self.__phone}\nEmail           :  {self.__email}\nAddress         :  {self.__address}"
