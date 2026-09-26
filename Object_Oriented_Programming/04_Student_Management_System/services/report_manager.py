from repositories.student_repository import StudentRepository
from repositories.course_repository import CourseRepository
from repositories.course_offering_repository import CourseOfferingRepository
from repositories.enrollment_repository import EnrollmentRepository


class ReportManager:

    GRADE_POINTS = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D": 1.0,
        "F": 0.0
    }

    def __init__(self):
        self.student_repository = StudentRepository()
        self.course_repository = CourseRepository()
        self.course_offering_repository = CourseOfferingRepository()
        self.enrollment_repository = EnrollmentRepository()

    def student_transcript(self):

        student_id = input("Enter Student ID: ")

        student = self.student_repository.find_by_id(student_id)

        if student is None:
            return "Student is not found.\n"

        enrollments = (
            self.enrollment_repository
            .find_by_student(student_id)
        )

        if not enrollments:
            return (
                f"Student: {student.first_name} "
                f"{student.last_name}\n"
                "No enrollment records found.\n"
            )

        output = ""

        output += "========================================\n"
        output += "           STUDENT TRANSCRIPT\n"
        output += "========================================\n\n"

        output += f"Student ID    : {student.student_id}\n"
        output += f"Student Name  : {student.first_name} {student.last_name}\n"
        output += f"Student Type  : {student.student_type}\n"
        output += f"Department    : {student.department}\n"
        output += f"Status        : {student.status}\n\n"

        output += "----------------------------------------\n"
        output += "COURSE HISTORY\n"
        output += "----------------------------------------\n"

        for enrollment in enrollments:

            offering = (
                self.course_offering_repository
                .find_by_id(enrollment.offering_id)
            )

            if offering is None:
                continue

            course = (
                self.course_repository
                .find_by_id(offering.course_id)
            )

            if course is None:
                continue

            output += (
                f"Course Code   : {course.course_code}\n"
                f"Course Name   : {course.course_name}\n"
                f"Credit Hours  : {course.credit_hours}\n"
                f"Semester      : {offering.semester}\n"
                f"Academic Year : {offering.academic_year}\n"
                f"Grade         : "
                f"{enrollment.grade if enrollment.grade else 'N/A'}\n"
                f"Status        : {enrollment.status}\n"
            )

            output += "----------------------------------------\n"

        return output

    def student_gpa(self):

        student_id = input("Enter Student ID: ")

        student = self.student_repository.find_by_id(student_id)

        if student is None:
            return "Student is not found.\n"

        enrollments = (
            self.enrollment_repository
            .find_by_student(student_id)
        )

        total_quality_points = 0
        total_credit_hours = 0
        completed_courses = 0

        for enrollment in enrollments:

            if enrollment.status != "COMPLETED":
                continue

            if not enrollment.grade:
                continue

            grade_point = self.GRADE_POINTS.get(
                enrollment.grade
            )

            if grade_point is None:
                continue

            offering = (
                self.course_offering_repository
                .find_by_id(enrollment.offering_id)
            )

            if offering is None:
                continue

            course = (
                self.course_repository
                .find_by_id(offering.course_id)
            )

            if course is None:
                continue

            credit_hours = int(course.credit_hours)

            total_quality_points += (
                grade_point * credit_hours
            )

            total_credit_hours += credit_hours
            completed_courses += 1

        if total_credit_hours == 0:
            return (
                f"Student: {student.first_name} "
                f"{student.last_name}\n"
                "No completed courses available for GPA calculation.\n"
            )

        gpa = (
            total_quality_points /
            total_credit_hours
        )

        output = ""

        output += "========================================\n"
        output += "              STUDENT GPA\n"
        output += "========================================\n\n"

        output += f"Student ID       : {student.student_id}\n"
        output += (
            f"Student Name     : "
            f"{student.first_name} {student.last_name}\n"
        )
        output += f"Completed Courses: {completed_courses}\n"
        output += f"Credit Hours     : {total_credit_hours}\n"
        output += f"GPA              : {gpa:.2f}\n"

        return output

    def course_enrollment_report(self):

        offering_id = input("Enter Offering ID: ")

        offering = (
            self.course_offering_repository
            .find_by_id(offering_id)
        )

        if offering is None:
            return "Course offering is not found.\n"

        course = (
            self.course_repository
            .find_by_id(offering.course_id)
        )

        if course is None:
            return "Course is not found.\n"

        enrollments = (
            self.enrollment_repository
            .find_by_offering(offering_id)
        )

        current_enrollment_count = 0

        for enrollment in enrollments:
            if enrollment.status == "ENROLLED":
                current_enrollment_count += 1

        available_seats = (
            int(offering.capacity) -
            current_enrollment_count
        )

        occupancy = 0

        if int(offering.capacity) > 0:
            occupancy = (
                current_enrollment_count /
                int(offering.capacity)
            ) * 100

        output = ""

        output += "========================================\n"
        output += "       COURSE ENROLLMENT REPORT\n"
        output += "========================================\n\n"

        output += f"Offering ID    : {offering.offering_id}\n"
        output += f"Course Code    : {course.course_code}\n"
        output += f"Course Name    : {course.course_name}\n"
        output += f"Semester       : {offering.semester}\n"
        output += f"Academic Year  : {offering.academic_year}\n\n"

        output += "----------------------------------------\n"
        output += "ENROLLMENT SUMMARY\n"
        output += "----------------------------------------\n"

        output += f"Capacity       : {offering.capacity}\n"
        output += (
            f"Currently Enrolled : "
            f"{current_enrollment_count}\n"
        )
        output += f"Available Seats: {available_seats}\n"
        output += f"Occupancy      : {occupancy:.1f}%\n\n"

        output += "----------------------------------------\n"
        output += "STUDENTS\n"
        output += "----------------------------------------\n"

        if not enrollments:
            output += "No students have enrolled.\n"
            return output

        for enrollment in enrollments:

            student = (
                self.student_repository
                .find_by_id(enrollment.student_id)
            )

            if student is None:
                continue

            output += (
                f"Student ID   : {student.student_id}\n"
                f"Student Name : "
                f"{student.first_name} {student.last_name}\n"
                f"Status       : {enrollment.status}\n"
                f"Grade        : "
                f"{enrollment.grade if enrollment.grade else 'N/A'}\n"
            )

            output += "----------------------------------------\n"

        return output

    def department_report(self):

        department_id = input("Enter Department ID: ")

        students = self.student_repository.find_all()
        courses = self.course_repository.find_all()

        department_students = []

        for student in students:
            if student.department == department_id:
                department_students.append(student)

        department_courses = []

        for course in courses:
            if course.department_id == department_id:
                department_courses.append(course)

        if not department_students and not department_courses:
            return "Department is not found or has no records.\n"

        output = ""

        output += "========================================\n"
        output += "          DEPARTMENT REPORT\n"
        output += "========================================\n\n"

        output += f"Department ID : {department_id}\n\n"

        output += "----------------------------------------\n"
        output += "STUDENT STATISTICS\n"
        output += "----------------------------------------\n"

        output += (
            f"Total Students : "
            f"{len(department_students)}\n"
        )

        undergraduate = 0
        graduate = 0
        phd = 0

        active = 0
        on_leave = 0
        suspended = 0
        graduated = 0
        withdrawn = 0

        for student in department_students:

            if student.student_type == "UNDERGRADUATE":
                undergraduate += 1

            elif student.student_type == "GRADUATE":
                graduate += 1

            elif student.student_type == "PHD":
                phd += 1

            if student.status == "ACTIVE":
                active += 1

            elif student.status == "ON_LEAVE":
                on_leave += 1

            elif student.status == "SUSPENDED":
                suspended += 1

            elif student.status == "GRADUATED":
                graduated += 1

            elif student.status == "WITHDRAWN":
                withdrawn += 1

        output += f"Undergraduate  : {undergraduate}\n"
        output += f"Graduate       : {graduate}\n"
        output += f"PhD            : {phd}\n\n"

        output += f"Active         : {active}\n"
        output += f"On Leave       : {on_leave}\n"
        output += f"Suspended      : {suspended}\n"
        output += f"Graduated      : {graduated}\n"
        output += f"Withdrawn      : {withdrawn}\n\n"

        output += "----------------------------------------\n"
        output += "COURSE STATISTICS\n"
        output += "----------------------------------------\n"

        output += (
            f"Total Courses  : "
            f"{len(department_courses)}\n"
        )

        return output

    def student_statistics(self):

        students = self.student_repository.find_all()

        if not students:
            return "No students found.\n"

        total_students = len(students)

        undergraduate = 0
        graduate = 0
        phd = 0

        active = 0
        on_leave = 0
        suspended = 0
        graduated = 0
        withdrawn = 0

        male = 0
        female = 0

        for student in students:

            if student.student_type == "UNDERGRADUATE":
                undergraduate += 1

            elif student.student_type == "GRADUATE":
                graduate += 1

            elif student.student_type == "PHD":
                phd += 1

            if student.status == "ACTIVE":
                active += 1

            elif student.status == "ON_LEAVE":
                on_leave += 1

            elif student.status == "SUSPENDED":
                suspended += 1

            elif student.status == "GRADUATED":
                graduated += 1

            elif student.status == "WITHDRAWN":
                withdrawn += 1

            if student.gender == "MALE":
                male += 1

            elif student.gender == "FEMALE":
                female += 1

        output = ""

        output += "========================================\n"
        output += "          STUDENT STATISTICS\n"
        output += "========================================\n\n"

        output += f"Total Students : {total_students}\n\n"

        output += "----------------------------------------\n"
        output += "BY STUDENT TYPE\n"
        output += "----------------------------------------\n"

        output += f"Undergraduate  : {undergraduate}\n"
        output += f"Graduate       : {graduate}\n"
        output += f"PhD            : {phd}\n\n"

        output += "----------------------------------------\n"
        output += "BY STATUS\n"
        output += "----------------------------------------\n"

        output += f"Active         : {active}\n"
        output += f"On Leave       : {on_leave}\n"
        output += f"Suspended      : {suspended}\n"
        output += f"Graduated      : {graduated}\n"
        output += f"Withdrawn      : {withdrawn}\n\n"

        output += "----------------------------------------\n"
        output += "BY GENDER\n"
        output += "----------------------------------------\n"

        output += f"Male           : {male}\n"
        output += f"Female         : {female}\n"

        return output