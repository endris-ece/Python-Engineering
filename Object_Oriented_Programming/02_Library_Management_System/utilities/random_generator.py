import random
import csv
class RandomGenerator:
    rand = random.randint(1000, 10000)

    def generate_book_id(self):
        while True:
            exist = False
            book_id = f"b{self.rand}"
            with open("books.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["book_id"] == book_id:
                        exist = True
            if not exist:
                return book_id
                
    def generate_loan_id(self):
        while True:
            exist = False
            loan_id = f"l{self.rand}"
            with open("loans.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["loan_id"] == loan_id:
                        exist = True
            if not exist:
                return loan_id

    def generate_member_id(self):
        while True:
            exist = False
            member_id = f"m{self.rand}"
            with open("members.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["member_id"] == member_id:
                        exist = True
            if not exist:
                return member_id