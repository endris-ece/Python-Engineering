from exceptions import InvalidNameError,InvalidDateError,InvalidPhoneNumberError,InvalidEmailError, InvalidCourseCodeError, InvalidCourseNameError, InvalidCreditHoursError, InvalidGradeError, InvalidCapacityError
from datetime import date
import re

class Validator:

    def validate_name(self, name):
        name = name.strip()
        if not name.isalpha():
            raise InvalidNameError("Name must only contain alphabets!!\n")
        return name

    def validate_date_of_birth(self, year, month, day):
        date_of_birth = date(int(year), int(month), int(day))
        try:

            if not(date_of_birth.year <= 2015 and date_of_birth.year >= 1975):
                raise ValueError
            return date_of_birth
        except ValueError:
            raise InvalidDateError("Invalid Date!!\n")

    def validate_phone(self, phone):
        phone = phone.strip()
        if not (phone.isdigit() and len(phone) == 10 and phone.startswith("0")):
            raise InvalidPhoneNumberError(phone)
        return f"+251 {phone[1:]}"

    def validate_email(self, email):
        email = email.strip()
        if not email:
            raise InvalidEmailError("Email cannot be empty.")

        if email.count("@") != 1:
            raise InvalidEmailError("Invalid email format.")

        username, domain = email.split("@")
        if not username or not domain:
            raise InvalidEmailError("Invalid email format.")

        if domain != "aau.edu.et":
            raise InvalidEmailError("Use your university email.")

        return email

    def validate_course_code(self, course_code):
        course_code = course_code.strip().upper()
        if not course_code:
            raise InvalidCourseCodeError("Course code cannot be empty!!\n")
        if not re.fullmatch(r"[A-Z]{2,5}\d{3,4}", course_code):
            raise InvalidCourseCodeError(
                "Invalid course code. Example: ECE2101"
            )
        return course_code

    def validate_course_name(self, course_name):
        course_name = course_name.strip()
        if not course_name:
            raise InvalidCourseNameError("Course name cannot be empty.")
        if len(course_name) > 100:
            raise InvalidCourseNameError("Course name is too long.")
        return course_name

    def validate_credit_hours(self, credit_hours):
        try:
            credit_hours = int(credit_hours)
        except ValueError:
            raise InvalidCreditHoursError("Credit hours must be a whole number.")
        if not 1 <= credit_hours <= 6:
            raise InvalidCreditHoursError("Credit hours must be between 1 and 6.")
        return credit_hours
    
    def validate_grade(self, grade):
        grade = grade.strip().upper()

        if not grade:
            raise InvalidGradeError("Grade cannot be empty!!\n")
        if not grade in ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]:
            raise InvalidGradeError("Invalid Grade!!\n")
        return grade

    def validate_capacity(self, capacity):
        try:
            capacity = int(capacity)
        except ValueError:
            raise InvalidCapacityError(
                "Capacity must be a whole number."
            )

        if capacity <= 0:
            raise InvalidCapacityError(
                "Capacity must be greater than zero."
            )

        return capacity