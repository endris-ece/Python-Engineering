from models.student import Student
from utilities.validators import Validator
from utilities.random_generator import RandomGenerator
from utilities.menus import Menu
from exceptions import InvalidNameError,InvalidDateError,InvalidPhoneNumberError,InvalidEmailError
from repositories.student_repository import StudentRepository
from enum import Enum
from datetime import date

class UpdateMenu(Enum):
    FIRST_NAME = 1
    LAST_NAME = 2
    DATE_OF_BIRTH = 3
    GENDER = 4
    PHONE = 5
    EMAIL = 6
    STUDENT_TYPE = 7
    DEPARTMENT = 8
    STATUS = 9
    EXIT = 10


class StudentType(Enum):
    UNDERGRADUATE = 1
    GRADUATE = 2
    PHD = 3

class Gender(Enum):
    MALE = 1
    FEMALE = 2

class StudentStatus(Enum):
    ACTIVE = 1
    ON_LEAVE = 2
    SUSPENDED = 3
    GRADUATED = 4
    WITHDRAWN = 5

class StudentManager:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.menu = Menu()
        self.validator = Validator()
        self.student_repository = StudentRepository()

    def add_student(self):
        while True:
            try:
                student_type = self.menu.generate_menu(StudentType).name
                student_id = self.random_generator.generate_student_id(student_type)
                first_name = self.validator.validate_name(input("Enter first name: "))
                last_name = self.validator.validate_name(input("Enter last name: "))
                print("Enter Birth Date (yyyy-mm-dd): ")
                year = input("Enter the year: ")
                month = input("Enter the month: ")
                day = input("Enter the day: ")
                birth_day = self.validator.validate_date_of_birth(year, month, day)
                gender = self.menu.generate_menu(Gender).name
                phone = self.validator.validate_phone(input("Enter phone number: "))
                email = self.validator.validate_email(input("Enter email: "))
                department = self.menu.select_department()
                status = self.menu.generate_menu(StudentStatus).name
                student = Student(student_id, first_name, last_name, birth_day, gender, phone, email, student_type, department, status)
                break
            except InvalidDateError as e:
                print(e)
            except InvalidEmailError as e:
                print(e)
            except InvalidNameError as e:
                print(e)
            except InvalidPhoneNumberError as e:
                print(e)
        self.student_repository.save(student)
        return student

    def view_students(self):
        students = self.student_repository.find_all()
        return "\n".join(str(student) for student in students)

    def search_student(self):
        student_id = input("Enter student ID: ")
        student = self.student_repository.find_by_id(student_id)
        if student is None:
            return f"Student Not Found!!\n"
        return student

    def update_student(self):
        student_id = input("Enter the student ID: ")
        student = self.student_repository.find_by_id(student_id)
        if student is None:
            return f"Student Not Found!!\n"
        while True:
            try:
                option = self.menu.generate_menu(UpdateMenu)
                match option:
                    case UpdateMenu.FIRST_NAME:
                        first_name = self.validator.validate_name(input("Enter first name: "))
                        student.first_name = first_name
                    case UpdateMenu.LAST_NAME:
                        last_name = self.validator.validate_name(input("Enter last name: "))
                        student.last_name = last_name
                    case UpdateMenu.DATE_OF_BIRTH:
                        year = input("Enter the year: ")
                        month = input("Enter the month: ")
                        day = input("Enter the day: ")
                        birth_day = self.validator.validate_date_of_birth(year, month, day)
                        student.date_of_birth = birth_day
                    case UpdateMenu.GENDER:
                        gender = self.menu.generate_menu(Gender).name
                        student.gender = gender
                    case UpdateMenu.PHONE:
                        phone = self.validator.validate_phone(input("Enter phone number: "))
                        student.phone = phone
                    case UpdateMenu.EMAIL:
                        email = self.validator.validate_email(input("Enter email: "))
                        student.email = email
                    case UpdateMenu.STUDENT_TYPE:
                        student_type = self.menu.generate_menu(StudentType).name
                        student.student_type = student_type
                    case UpdateMenu.DEPARTMENT:
                        department = self.menu.select_department()
                        student.department = department
                    case UpdateMenu.STATUS:
                        status = self.menu.generate_menu(StudentStatus).name
                        student.status = status
                    case UpdateMenu.EXIT:
                        break
            except InvalidDateError as e:
                print(e)
            except InvalidEmailError as e:
                print(e)
            except InvalidNameError as e:
                print(e)
            except InvalidPhoneNumberError as e:
                print(e)
                
        self.student_repository.update(student)
        return f"Student updated successfully."
      
    def delete_student(self):
        student_id = input("Enter student ID: ")
        student = self.student_repository.delete(student_id)
        if not student:
            return f"Student not Found!!\n"
        return f"Delete succefful!!\n"
