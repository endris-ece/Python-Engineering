
from utilities.menus import Menu
from utilities.random_generator import RandomGenerator
from utilities.validators import Validator
from models.course_offering import CourseOffering
from exceptions import CourseNotFoundError, InvalidAcademicYearError, InvalidCapacityError
from repositories.course_offering_repository import CourseOfferingRepository
from repositories.course_repository import CourseRepository
from repositories.enrollment_repository import EnrollmentRepository
from enum import Enum

class Semester(Enum):
    SEMESTER_I  = 1
    SEMESTER_II = 2
    SEMESTER_III = 3

class UpdateMenu(Enum):
    SEMESTER = 1
    ACADEMIC_YEAR = 2
    CAPACITY = 3
    EXIT = 4

class CourseOfferingManager:

    def __init__(self):
        self.course_offering_repository = CourseOfferingRepository()
        self.course_repository = CourseRepository()
        self.enrollment_repository = EnrollmentRepository()
        self.random_generator = RandomGenerator()
        self.validator = Validator()
        self.menu = Menu()

    def add_offering(self):
        while True:
            try:
                        
                offering_id = self.random_generator.generate_offering_id()
                course = self.course_repository.find_by_id(input('Enter Course ID: '))
                if course is None:
                    raise CourseNotFoundError
                course_id = course.course_id
                semester = self.menu.generate_menu(Semester).name
                academic_year = input("Enter the year(yyyy/yy): ").strip()
                if not academic_year in ["2026/27", "2027/28", "2028/29", "2029/30"]:
                    raise InvalidAcademicYearError
                capacity = self.validator.validate_capacity(input("Enter Capacity: "))
                break
            except InvalidCapacityError as e:
                print(e)
            except CourseNotFoundError:
                print("Course is Not Found!!\n")
            except InvalidAcademicYearError:
                print("Invalid Academic Year!!\n")
         
        course_offering = CourseOffering(offering_id, course_id, semester, academic_year, capacity)
        self.course_offering_repository.save(course_offering)
        return course_offering

    def view_offerings(self):
        course_offerings = (self.course_offering_repository.find_all())
        return "\n".join(
            str(offering)
            for offering in course_offerings)

    def search_offering(self):
        offering_id = input("Enter Offering ID: ")
        offering = self.course_offering_repository.find_by_id(offering_id)
        if offering == None:
            return f"Course Offering is Not Found!!\n"
        return offering

    def update_offering(self):
        offering_id = input("Enter Offering ID: ")
        offering = self.course_offering_repository.find_by_id(offering_id)
        if offering == None:
            return f"Course Offering is Not Found!!\n"
        while True:
            try:
                option = self.menu.generate_menu(UpdateMenu)
                match option:
                    case UpdateMenu.SEMESTER:
                        semester = self.menu.generate_menu(Semester).name
                        offering.semester = semester
                    case UpdateMenu.ACADEMIC_YEAR:
                        academic_year = input("Enter the year(yyyy/yy): ").strip()
                        if not academic_year in ["2026/27", "2027/28", "2028/29", "2029/30"]:
                            raise InvalidAcademicYearError
                        offering.academic_year = academic_year
                    case UpdateMenu.CAPACITY:

                        capacity = self.validator.validate_capacity(input("Enter Capacity: "))
                        enrollments = (self.enrollment_repository.find_by_offering(offering.offering_id))
                        if capacity < len(enrollments):
                            print(
                                f"Capacity cannot be less than the "
                                f"current enrollment count ({len(enrollments)})."
                            )
                            continue
                        offering.capacity = capacity
                    case EXIT:
                        break
            except InvalidCapacityError as e:
                print(e)
            except InvalidAcademicYearError:
                print("Invalid Academic Year!!\n")

        self.course_offering_repository.update(offering)
        return f"Update succefull!!\n"
        
    def delete_offering(self):
        offering_id = input("Enter Offering ID: ")
        offering = (self.course_offering_repository.find_by_id(offering_id))
        if offering is None:
            return "Course offering is not found.\n"
        enrollments = (self.enrollment_repository.find_by_offering(offering_id))
        if enrollments:
            return (
                "Cannot delete this course offering because "
                "students are enrolled in it.\n"
            )
        self.course_offering_repository.delete(offering_id)
        return "Course offering deleted successfully.\n"