import random
from enum import Enum
import csv
from pathlib import Path
from repositories.student_repository import StudentRepository
from repositories.course_repository import CourseRepository
from repositories.enrollment_repository import EnrollmentRepository
from repositories.course_offering_repository import CourseOfferingRepository

student_repo = StudentRepository()
enrollment_repo = EnrollmentRepository()
course_repo = CourseRepository()
course_offering_repo = CourseOfferingRepository()

class StudentType(Enum):
    UNDERGRADUATE = 1
    GRADUATE = 2
    PHD = 3

BASE_DIR = Path(__file__).resolve().parent.parent
STUDENT_FILE = BASE_DIR / "data" / "students.csv"  
ENROLLMENT_FILE = BASE_DIR / "data" / "enrollments.csv"
COURSE_FILE = BASE_DIR / "data" / "courses.csv"
OFFERING_FILE = BASE_DIR / "data" / "course_offerings.csv"

class RandomGenerator:

    def generate_student_id(self, student_type):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            if StudentType[student_type] == StudentType.UNDERGRADUATE:
                student_id = f"UGR/{rand}/19"
            elif StudentType[student_type] == StudentType.GRADUATE:
                student_id = f"GR/{rand}/19"
            elif StudentType[student_type] == StudentType.PHD:
                student_id = f"PHD/{rand}/19"
            student = student_repo.find_by_id(student_id)
            if student is None:
                return student_id
                
    def generate_enrollment_id(self):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            enrollment_id = f"enroll{rand}"
            enrollment = enrollment_repo.find_by_id(enrollment_id)
            if enrollment is None:
                return enrollment_id

    def generate_course_id(self):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            course_id = f"course{rand}"
            course = course_repo.find_by_id(course_id)
            if course is None:
                return course_id

    def generate_offering_id(self):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            offering_id = f"offer{rand}"
            offering = course_offering_repo.find_by_id(offering_id)
            if offering is None:
                return offering_id