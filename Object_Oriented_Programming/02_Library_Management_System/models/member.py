from exceptions import InvalidEmailError, InvalidNameError, InvalidPhoneNumberError

class Member:

    def __init__(self, member_id, first_name, last_name, phone_number, email, address, registration_date):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.registration_date = registration_date

    @property
    def member_id(self):
        return self.__member_id

    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name

    @property
    def phone_number(self):
        return self.__phone_number
    
    @property
    def email(self):
        return self.__email

    @property
    def address(self):
        return self.__address
    
    @property
    def registration_date(self):
        return self.__registration_date
        
    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id
    
    @first_name.setter
    def first_name(self, first_name):
        if not first_name.isalpha():
            raise InvalidNameError(first_name)
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, second_name):
        if not second_name.isalpha():
            raise InvalidNameError(second_name)
        self.__last_name = second_name
    
    @phone_number.setter
    def phone_number(self, phone):
        if not (phone.isdigit() and len(phone) == 10 and phone.startswith("0")):
            raise InvalidPhoneNumberError(phone)
        self.__phone_number = f"+251 {phone[1:]}"

    @email.setter
    def email(self, email):
        if not ("@" in email and email.endswith(".com")):
            raise InvalidEmailError(email)
        self.__email = email
    
    @address.setter
    def address(self, address):
        for char in address:
            if not (char in [" ", "/", "."] or char.isalnum()):
                raise InvalidNameError(address)
        self.__address = address
    
    @registration_date.setter
    def registration_date(self, date):
        self.__registration_date = date
    
    def __str__(self):
        return f"Full name       :  {self.__first_name} {self.__last_name}\nMember ID       :  {self.__member_id}\nPhone           :  {self.__phone_number}\nEmail           :  {self.__email}\nAddress         :  {self.__address}\nRegistration Date:  {self.__registration_date}"
