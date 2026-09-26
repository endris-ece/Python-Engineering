from utilities.menus import Menu
from models.course import Course
import csv
from pathlib import Path

menu = Menu()

BASE_DIR = Path(__file__).resolve().parent.parent
COURSE_FILE = BASE_DIR / "data" / "courses.csv"
DEPARTMENT_FILE = BASE_DIR / "data" / "departments.csv"

class CourseRepository:
    
    def save(self, course):
        row = [course.course_id, course.course_code, course.course_name, course.credit_hours, course.department_id]
        with open(COURSE_FILE, 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def find_all(self):
        courses = []
        with open(COURSE_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                course = Course(row["course_id"],row["course_code"],row["course_name"],row["credit_hours"],row["department_id"])
                courses.append(course)
        return courses

    def find_by_id(self, course_id):
        with open(COURSE_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["course_id"] == course_id:
                    return Course(row["course_id"],row["course_code"],row["course_name"],row["credit_hours"],row["department_id"])
        return None
    def find_by_code(self, course_code):
        with open(COURSE_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["course_code"] == course_code:
                    return Course(row["course_id"],row["course_code"],row["course_name"],row["credit_hours"],row["department_id"])
        return None

    def delete(self, course_id):
        found = False
        updated = []
        with open(COURSE_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["course_id"] == course_id:
                    found = True
                    continue
                updated.append(row)
            if not found:
                return False
        with open(COURSE_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated)

        return True

    def update(self, course):
        rows = []
        with open(COURSE_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if course.course_id == row["course_id"]:
                    rows.append({"course_id": course.course_id, "course_code": course.course_code, "course_name": course.course_name, "credit_hours": course.credit_hours, "department_id": course.department_id})
                    continue
                rows.append(row)
        
        with open(COURSE_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(rows)

