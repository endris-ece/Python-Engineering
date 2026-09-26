
class Student:

    def __init__(self, student_id, first_name, last_name, date_of_birth, gender, phone, email, student_type, department, status):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone = phone
        self.email = email
        self.student_type = student_type
        self.department = department
        self.status = status
    
    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth
    
    @property
    def gender(self):
        return self.__gender

    @property
    def phone(self):
        return self.__phone
    
    @property
    def email(self):
        return self.__email
    
    @property
    def student_type(self):
        return self.__student_type

    @property
    def department(self):
        return self.__department

    @property
    def status(self):
        return self.__status

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id
        
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email

    @student_type.setter
    def student_type(self, student_type):
        self.__student_type = student_type

    @department.setter
    def department(self, department):
        self.__department = department

    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        return f"|Student ID     : {self.student_id}\n|Full Name      : {self.first_name} {self.last_name}\n|Date of Birth  : {self.date_of_birth}\n|Gender         : {self.gender}\n|Phone Number   : {self.phone}\n|Email          : {self.email}\n|Student Type   : {self.student_type}\n|Department     : {self.department}\n|Status         : {self.status}\n\n"
