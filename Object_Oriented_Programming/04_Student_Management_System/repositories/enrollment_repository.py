from utilities.menus import Menu
from models.enrollment import Enrollment
import csv
from pathlib import Path

menu = Menu()

BASE_DIR = Path(__file__).resolve().parent.parent
ENROLLMENT_FILE = BASE_DIR / "data" / "enrollments.csv"

class EnrollmentRepository:
    
    def save(self, enrollment):
        row = [enrollment.enrollment_id, enrollment.student_id, enrollment.offering_id, enrollment.grade, enrollment.status]
        with open(ENROLLMENT_FILE, 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def find_all(self):
        enrollments = []

        with open(ENROLLMENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                enrollment = Enrollment(row["enrollment_id"],row["student_id"],row["offering_id"],row["grade"],row["status"])
                enrollments.append(enrollment)

        return enrollments

    def find_by_id(self, enrollment_id):
        with open(ENROLLMENT_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["enrollment_id"] == enrollment_id:
                    return Enrollment(row["enrollment_id"],row["student_id"],row["offering_id"],row["grade"],row["status"])
        return None

    def delete(self, enrollment_id):
        found = False
        updated = []
        with open(ENROLLMENT_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["enrollment_id"] == enrollment_id:
                    found = True
                    continue
                updated.append(row)
            if not found:
                return False
        with open(ENROLLMENT_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated)

        return True

    def update(self, enrollment):
        rows = []
        with open(ENROLLMENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if enrollment.enrollment_id == row["enrollment_id"]:
                    rows.append({"enrollment_id": enrollment.enrollment_id, "student_id": enrollment.student_id, "offering_id": enrollment.offering_id, "grade": enrollment.grade, "status": enrollment.status})
                    continue
                rows.append(row)
        
        with open(ENROLLMENT_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(rows)
    
    def find_by_student_and_offering(self, student_id, offering_id):
        with open(ENROLLMENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if (
                    row["student_id"] == student_id
                    and row["offering_id"] == offering_id
                ):
                    return Enrollment(
                        row["enrollment_id"],
                        row["student_id"],
                        row["offering_id"],
                        row["grade"],
                        row["status"]
                    )

        return None

    def find_by_offering(self, offering_id):
        enrollments = []

        with open(ENROLLMENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["offering_id"] == offering_id:
                    enrollments.append(
                        Enrollment(
                            row["enrollment_id"],
                            row["student_id"],
                            row["offering_id"],
                            row["grade"],
                            row["status"]
                        )
                    )

        return enrollments

    def find_by_student(self, student_id):
        enrollments = []

        with open(ENROLLMENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["student_id"] == student_id:
                    enrollments.append(
                        Enrollment(
                            row["enrollment_id"],
                            row["student_id"],
                            row["offering_id"],
                            row["grade"],
                            row["status"]
                        )
                    )

        return enrollments