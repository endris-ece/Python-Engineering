from services.student_manager import StudentManager
from services.course_manager import CourseManager
from services.report_manager import ReportManager
from services.enrollment_manager import EnrollmentManager
from services.course_offering_manager import CourseOfferingManager
from enum import Enum
from utilities.menus import Menu

menu = Menu()
student_manager = StudentManager()
course_manager = CourseManager()
enrollment_manager = EnrollmentManager()
course_offering_manager = CourseOfferingManager()
report_manager = ReportManager()


class MainMenu(Enum):
    STUDENT_MANAGEMENT = 1
    COURSE_MANAGEMENT = 2
    ENROLLMENT_MANAGEMENT = 3
    COURSE_OFFERING = 4
    REPORTS = 5
    EXIT = 6

class StudentMenu(Enum):
    ADD_STUDENT = 1
    VIEW_STUDENTS = 2
    SEARCH_STUDENT = 3
    UPDATE_STUDENT = 4
    DELETE_STUDENT = 5
    EXIT = 6

class CourseMenu(Enum):
    ADD_COURSE = 1
    VIEW_COURSES = 2
    SEARCH_COURSE = 3
    UPDATE_COURSE = 4
    DELETE_COURSE = 5
    EXIT = 6

class EnrollmentMenu(Enum):
    ENROLL_STUDENT = 1
    VIEW_ENROLLMENTS = 2
    SEARCH_ENROLLMENT = 3
    UPDATE_ENROLLMENT = 4
    DELETE_ENROLLMENT = 5
    EXIT = 6

class CourseOfferingMenu(Enum):
    ADD_OFFERING = 1
    VIEW_OFFERINGS = 2
    SEARCH_OFFERING = 3
    UPDATE_OFFERING = 4
    DELETE_OFFERING = 5
    EXIT = 6

class ReportsMenu(Enum):
    STUDENT_TRANSCRIPT = 1
    STUDENT_GPA = 2
    COURSE_ENROLLMENT_REPORT = 3
    DEPARTMENT_REPORT = 4
    STUDENT_STATISTICS = 5
    EXIT = 6

def student_management():

    operations = {
        StudentMenu.ADD_STUDENT: student_manager.add_student,
        StudentMenu.VIEW_STUDENTS: student_manager.view_students,
        StudentMenu.SEARCH_STUDENT: student_manager.search_student,
        StudentMenu.UPDATE_STUDENT: student_manager.update_student,
        StudentMenu.DELETE_STUDENT: student_manager.delete_student
    }
    print("*******************************************")
    print("\tSTUDENT MANAGER")
    print("*******************************************\n")
    option = menu.generate_menu(StudentMenu)
    while option != StudentMenu.EXIT:
        print(operations[option]())
        option = menu.generate_menu(StudentMenu)

def course_management():

    operations = {
        CourseMenu.ADD_COURSE: course_manager.add_course,
        CourseMenu.VIEW_COURSES: course_manager.view_courses,
        CourseMenu.SEARCH_COURSE: course_manager.search_course,
        CourseMenu.UPDATE_COURSE: course_manager.update_course,
        CourseMenu.DELETE_COURSE: course_manager.delete_course
    }
    print("*******************************************")
    print("\tCOURSE MANAGER")
    print("*******************************************\n")
    option = menu.generate_menu(CourseMenu)
    while option != CourseMenu.EXIT:
        print(operations[option]())
        option = menu.generate_menu(CourseMenu)

def enrollment_management():

    operations = {
        EnrollmentMenu.ENROLL_STUDENT: enrollment_manager.enroll_student,
        EnrollmentMenu.VIEW_ENROLLMENTS: enrollment_manager.view_enrollments,
        EnrollmentMenu.SEARCH_ENROLLMENT: enrollment_manager.search_enrollment,
        EnrollmentMenu.UPDATE_ENROLLMENT: enrollment_manager.update_enrollment,
        EnrollmentMenu.DELETE_ENROLLMENT: enrollment_manager.delete_enrollment
    }
    print("*******************************************")
    print("\tEnrollment MANAGER")
    print("*******************************************\n")
    option = menu.generate_menu(EnrollmentMenu)
    while option != EnrollmentMenu.EXIT:
        print(operations[option]())
        option = menu.generate_menu(EnrollmentMenu)

def course_offering_management():

    operations = {
        CourseOfferingMenu.ADD_OFFERING: course_offering_manager.add_offering,
        CourseOfferingMenu.VIEW_OFFERINGS: course_offering_manager.view_offerings,
        CourseOfferingMenu.SEARCH_OFFERING: course_offering_manager.search_offering,
        CourseOfferingMenu.UPDATE_OFFERING: course_offering_manager.update_offering,
        CourseOfferingMenu.DELETE_OFFERING: course_offering_manager.delete_offering
    }
    print("*******************************************")
    print("\tCOURSE OFFERING MANAGER")
    print("*******************************************\n")

    option = menu.generate_menu(CourseOfferingMenu)
    while option != CourseOfferingMenu.EXIT:
        print(operations[option]())
        option = menu.generate_menu(CourseOfferingMenu)

    
def reports():

    operations = {
        ReportsMenu.STUDENT_TRANSCRIPT: report_manager.student_transcript,
        ReportsMenu.STUDENT_GPA: report_manager.student_gpa,
        ReportsMenu.COURSE_ENROLLMENT_REPORT: report_manager.course_enrollment_report,
        ReportsMenu.DEPARTMENT_REPORT: report_manager.department_report,
        ReportsMenu.STUDENT_STATISTICS: report_manager.student_statistics
    }
    print("*******************************************")
    print("\tREPORTS")
    print("*******************************************\n")

    option = menu.generate_menu(ReportsMenu)
    
    while option != ReportsMenu.EXIT:
        print(operations[option]())
        option = menu.generate_menu(ReportsMenu)

def start():

    operations = {
        MainMenu.STUDENT_MANAGEMENT: student_management,
        MainMenu.COURSE_MANAGEMENT: course_management,
        MainMenu.ENROLLMENT_MANAGEMENT: enrollment_management,
        MainMenu.COURSE_OFFERING: course_offering_management,
        MainMenu.REPORTS: reports
    }
    print("*******************************************")
    print("\tSTUDENT MANAGEMENT SYSTEM")
    print("*******************************************\n")

    option = menu.generate_menu(MainMenu)
    while option != MainMenu.EXIT:
        operations[option]()
        option = menu.generate_menu(MainMenu)

start()