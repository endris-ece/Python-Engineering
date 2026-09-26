from models.course_offering import CourseOffering
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
COURSE_OFFERING_FILE = BASE_DIR / "data" / "course_offerings.csv"


class CourseOfferingRepository:
    
    def save(self, course_offering):
        row = [course_offering.offering_id, course_offering.course_id, course_offering.semester, course_offering.academic_year, course_offering.capacity]
        with open(COURSE_OFFERING_FILE, 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def find_all(self):
        course_offerings = []

        with open(COURSE_OFFERING_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                course_offering = CourseOffering(row["offering_id"],row["course_id"],row["semester"],row["academic_year"],row["capacity"])
                course_offerings.append(course_offering)

        return course_offerings

    def find_by_id(self, offering_id):
        with open(COURSE_OFFERING_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["offering_id"] == offering_id:
                    return CourseOffering(row["offering_id"],row["course_id"],row["semester"],row["academic_year"],row["capacity"])
        return None

    def delete(self, offering_id):
        found = False
        updated = []
        with open(COURSE_OFFERING_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["offering_id"] == offering_id:
                    found = True
                    continue
                updated.append(row)
            if not found:
                return False
        with open(COURSE_OFFERING_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated)

        return True

    def update(self, course_offering):
        rows = []
        with open(COURSE_OFFERING_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if course_offering.offering_id == row["offering_id"]:
                    rows.append({"offering_id": course_offering.offering_id, "course_id": course_offering.course_id, "semester": course_offering.semester, "academic_year": course_offering.academic_year, "capacity": course_offering.capacity})
                    continue
                rows.append(row)
        
        with open(COURSE_OFFERING_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(rows)
