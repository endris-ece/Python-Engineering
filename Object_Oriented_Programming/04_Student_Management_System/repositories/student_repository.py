from utilities.menus import Menu
from models.student import Student
import csv
from pathlib import Path

menu = Menu()

BASE_DIR = Path(__file__).resolve().parent.parent
STUDENT_FILE = BASE_DIR / "data" / "students.csv"


class StudentRepository:
    
    def save(self, student):
        row = [student.student_id, student.first_name, student.last_name, student.date_of_birth, student.gender, student.phone, student.email, student.student_type, student.department, student.status]
        with open(STUDENT_FILE, 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def find_all(self):
        students = []

        with open(STUDENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                student = Student(row["student_id"],row["first_name"],row["last_name"],row["date_of_birth"],row["gender"],row["phone"],row["email"],row["student_type"],row["department"],row["status"])
                students.append(student)

        return students

    def find_by_id(self, student_id):
        with open(STUDENT_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["student_id"] == student_id:
                    return Student(row["student_id"],row["first_name"],row["last_name"],row["date_of_birth"],row["gender"],row["phone"],row["email"],row["student_type"],row["department"],row["status"])
        return None

    def delete(self, student_id):
        found = False
        updated = []
        with open(STUDENT_FILE, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["student_id"] == student_id:
                    found = True
                    continue
                updated.append(row)
            if not found:
                return False
        with open(STUDENT_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated)

        return True
            
    def update(self, student):
        rows = []
        with open(STUDENT_FILE, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if student.student_id == row["student_id"]:
                    rows.append({
                        "student_id": student.student_id,
                        "first_name": student.first_name,
                        "last_name": student.last_name,
                        "date_of_birth": student.date_of_birth,
                        "gender": student.gender,
                        "phone": student.phone,
                        "email": student.email,
                        "student_type": student.student_type,
                        "department": student.department,
                        "status": student.status
                    })
                    continue
                rows.append(row)
        
        with open(STUDENT_FILE, 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(rows)

