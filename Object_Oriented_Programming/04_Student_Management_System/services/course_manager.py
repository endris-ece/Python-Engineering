from models.course import Course
from utilities.random_generator import RandomGenerator
from utilities.validators import Validator
from utilities.menus import Menu
from exceptions import InvalidCourseCodeError, InvalidCreditHoursError, InvalidCourseNameError
from repositories.course_repository import CourseRepository
from enum import Enum

class UpdateMenu(Enum):
    COURSE_CODE = 1
    COURSE_NAME = 2
    CREDIT_HOURS = 3
    DEPARTMENT_ID = 4
    EXIT = 5

class CourseManager:
    def __init__(self):
        self.random_generator = RandomGenerator()
        self.menu = Menu()
        self.validator = Validator()
        self.course_repository = CourseRepository()

    def add_course(self):
        while True:
            try:
                course_id = self.random_generator.generate_course_id()
                course_code = self.validator.validate_course_code(input("Enter Course Code: "))
                if self.course_repository.find_by_code(course_code):
                    raise InvalidCourseCodeError(
                        "Course code already exists!!"
                    )
                course_name = self.validator.validate_course_name(input("Enter Course Name: "))
                credit_hours = self.validator.validate_credit_hours(input("Enter Credit Hours: "))
                department_id = self.menu.select_department()
                break
            except InvalidCourseCodeError as e:
                print(e)
            except InvalidCourseNameError as e:
                print(e)
            except InvalidCreditHoursError as e:
                print(e)

        course = Course(course_id, course_code, course_name, credit_hours, department_id)
        self.course_repository.save(course)
        return course

    def view_courses(self):
        courses = self.course_repository.find_all()
        return "\n".join(str(course) for course in courses)

    def search_course(self):
        course_id = input("Enter course ID: ")
        course = self.course_repository.find_by_id(course_id)
        if course is None:
            return f"Course Not Found!!\n"
        return course

    def update_course(self):
        course_id = input("Enter Course ID: ")
        course = self.course_repository.find_by_id(course_id)
        if course == None:
            return f"Course Is Not Found!!\n"
        while True:
            try:
                option = self.menu.generate_menu(UpdateMenu)
                match option:
                    case UpdateMenu.COURSE_CODE:
                        course_code = self.validator.validate_course_code(input("Enter Course Code: "))
                        existing = self.course_repository.find_by_code(course_code)
                        if existing and existing.course_id != course.course_id:
                            raise InvalidCourseCodeError("Course code already exists!!")
                        course.course_code = course_code
                    case UpdateMenu.COURSE_NAME:
                        course_name = self.validator.validate_course_name(input("Enter Course Name: "))
                        course.course_name = course_name
                    case UpdateMenu.CREDIT_HOURS:
                        credit_hours = self.validator.validate_credit_hours(input("Enter Credit Hours: "))
                        course.credit_hours = credit_hours
                    case UpdateMenu.DEPARTMENT_ID:
                        department_id = self.menu.select_department()
                        course.department_id = department_id
                    case UpdateMenu.EXIT:
                        break
            except InvalidCourseCodeError as e:
                print(e)
            except InvalidCourseNameError as e:
                print(e)
            except InvalidCreditHoursError as e:
                print(e)

        self.course_repository.update(course)
        return f"Update succefull!!\n"
        
    def delete_course(self):
        course_id = input("Enter Course ID: ")
        delete = self.course_repository.delete(course_id)
        if delete:
            return f"Delete succefull!!\n"
        return f"Course Not Found!!!\n"
