from models.enrollment import Enrollment
from utilities.menus import Menu
from utilities.random_generator import RandomGenerator
from utilities.validators import Validator

from exceptions import (
    StudentNotFoundError,
    CourseOfferingNotFoundError,
    InvalidGradeError
)

from repositories.enrollment_repository import EnrollmentRepository
from repositories.student_repository import StudentRepository
from repositories.course_offering_repository import CourseOfferingRepository

from enum import Enum


class Status(Enum):
    ENROLLED = 1
    COMPLETED = 2
    DROPPED = 3


class UpdateMenu(Enum):
    GRADE = 1
    STATUS = 2


class EnrollmentManager:

    def __init__(self):
        self.random_generator = RandomGenerator()
        self.menu = Menu()
        self.validator = Validator()

        self.enrollment_repository = EnrollmentRepository()
        self.student_repository = StudentRepository()
        self.course_offering_repository = CourseOfferingRepository()

    def enroll_student(self):
        while True:
            try:
                student_id = input("Enter Student ID: ")

                student = self.student_repository.find_by_id(student_id)
                if student is None:
                    raise StudentNotFoundError(
                        "Student is not found."
                    )
                if student.status != "ACTIVE":
                    print(
                        f"Student cannot enroll because their status is "
                        f"{student.status}."
                    )
                    return

                offering_id = input("Enter Offering ID: ")

                offering = self.course_offering_repository.find_by_id(
                    offering_id
                )

                if offering is None:
                    raise CourseOfferingNotFoundError(
                        "Course offering is not found."
                    )

                existing = (
                    self.enrollment_repository
                    .find_by_student_and_offering(
                        student_id,
                        offering_id
                    )
                )

                if existing is not None:
                    print(
                        "Student is already enrolled in this course offering."
                    )
                    return

                enrollments = self.enrollment_repository.find_all()

                enrolled_count = 0

                for enrollment in enrollments:
                    if (
                        enrollment.offering_id == offering_id
                        and enrollment.status == "ENROLLED"
                    ):
                        enrolled_count += 1

                if enrolled_count >= int(offering.capacity):
                    print("Course offering is already full.")
                    return

                enrollment_id = (
                    self.random_generator.generate_enrollment_id()
                )

                grade = ""

                status = Status.ENROLLED.name

                enrollment = Enrollment(
                    enrollment_id,
                    student_id,
                    offering_id,
                    grade,
                    status
                )

                self.enrollment_repository.save(enrollment)

                return enrollment

            except StudentNotFoundError as e:
                print(e)

            except CourseOfferingNotFoundError as e:
                print(e)

            except InvalidGradeError as e:
                print(e)

    def view_enrollments(self):
        enrollments = self.enrollment_repository.find_all()

        return "\n".join(
            str(enrollment)
            for enrollment in enrollments
        )

    def search_enrollment(self):
        enrollment_id = input("Enter Enrollment ID: ")

        enrollment = self.enrollment_repository.find_by_id(
            enrollment_id
        )

        if enrollment is None:
            return "Enrollment is not found.\n"

        return enrollment

    def update_enrollment(self):
        enrollment_id = input("Enter Enrollment ID: ")

        enrollment = self.enrollment_repository.find_by_id(
            enrollment_id
        )

        if enrollment is None:
            return "Enrollment is not found.\n"

        while True:
            try:
                option = self.menu.generate_menu(UpdateMenu)

                match option:
                    case UpdateMenu.GRADE:

                        if enrollment.status != Status.COMPLETED.name:
                            print(
                                "Grade can only be changed for a "
                                "completed enrollment."
                            )
                            continue

                        grade = self.validator.validate_grade(
                            input("Enter Grade: ")
                        )

                        enrollment.grade = grade


                    case UpdateMenu.STATUS:

                        new_status = self.menu.generate_menu(Status).name

                        if new_status == Status.COMPLETED.name:

                            if enrollment.status == Status.COMPLETED.name:
                                print("Enrollment is already completed.")
                                continue

                            grade = self.validator.validate_grade(
                                input("Enter Grade: ")
                            )

                            enrollment.grade = grade
                            enrollment.status = Status.COMPLETED.name

                        elif new_status == Status.DROPPED.name:

                            enrollment.status = Status.DROPPED.name
                            enrollment.grade = ""

                        elif new_status == Status.ENROLLED.name:

                            enrollment.status = Status.ENROLLED.name
                            enrollment.grade = ""
                break

            except InvalidGradeError as e:
                print(e)

        self.enrollment_repository.update(enrollment)

        return "Enrollment updated successfully.\n"

    def delete_enrollment(self):
        enrollment_id = input("Enter Enrollment ID: ")

        deleted = self.enrollment_repository.delete(
            enrollment_id
        )

        if not deleted:
            return "Enrollment is not found.\n"

        return "Enrollment deleted successfully.\n"