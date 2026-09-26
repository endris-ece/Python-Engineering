import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEPARTMENT = BASE_DIR / "data" / "departments.csv"

class Menu:

    def generate_menu(self, menu):
        while True:
            try:
                for operation in menu:
                    print(f"{operation.value}. {operation.name}")
                option = int(input("Select an option: "))
                if option in range(1, operation.value + 1):
                    return menu(option)
                raise ValueError
            except ValueError:
                print(f"Input must be in [1,{operation.value}]!!\n")

    def select_department(self):
        while True:
            try:
                i = 1
                with open(DEPARTMENT, 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        print(f"{i}. {row['name']}")
                        i+=1
                option = int(input("Select an option: "))
                if option in range(1, i):
                    j=1
                    with open(DEPARTMENT, 'r', encoding="utf-8") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if j == option:
                                return row["department_id"]
                            j+=1
                raise ValueError
            except ValueError:
                print(f"Input must be in [1, {i-1}]!!\n")


