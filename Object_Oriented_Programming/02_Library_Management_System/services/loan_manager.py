from services.member_manager import MemberManager
from utilities.random_generator import RandomGenerator
from models.loan import Loan
from exceptions import MemberNotFoundError, BookNotFoundError, InvalidDateError, BookNotAvailableError
from datetime import date
import csv


class LoanManager:

    def __init__(self):
        self.member_manager = MemberManager()
        self.random_generator = RandomGenerator()

    def borrow_book(self):

        def get_member():
            while True:
                try:
                    print("Is the customer a member?")
                    print("1. Yes")
                    print("2. No")
                    exist = int(input(": "))
                    if exist == 1:
                        member_id = input("Enter Member Id: ")
                    elif exist == 2:
                        print("Register Member!\n")
                        customer = self.member_manager.register_member()
                        print(f"{customer}\n Take Member Id\n")
                        member_id = input("Enter Member Id: ")
                    else:
                        raise ValueError
                    return member_id
                except ValueError:
                    print("Invalid Input!\n")


        while True:
            try:
                book_found = False
                member_found = False
                loan_id = self.random_generator.generate_loan_id()
                member_id = get_member()
                with open("members.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["member_id"] == member_id:
                            member_found = True
                book_id = input("Enter Book Id: ")
                with open("books.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["book_id"] == book_id:
                            if int(row["available"]) < 1:
                                raise BookNotAvailableError
                            book_found = True
                borrow_date = date.today()
                print("Enter Due Date (yyyy-mm-dd): ")
                year = input("Enter the year: ")
                month = input("Enter the month: ")
                day = input("Enter the day: ")

                try:
                    due_date = date(int(year), int(month), int(day))
                except ValueError:
                    raise InvalidDateError(f"{year}-{month}-{day}")

                if due_date <= borrow_date:
                    raise InvalidDateError(due_date)

                returned = "No"
                if not member_found:
                    raise MemberNotFoundError(member_id)
                if not book_found:
                    raise BookNotFoundError(book_id)
                with open("loans.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["member_id"] == member_id and row["book_id"] == book_id:
                            return f"You can't borrow the same book twice!!\n"
                loan = Loan(loan_id, member_id, book_id, borrow_date, due_date, returned)
                break
            except BookNotFoundError as e:
                print(e)
            except InvalidDateError as e:
                print(e)
            except MemberNotFoundError as e:
                print(e)
            except BookNotAvailableError as e:
                print(e)

        row = [loan.loan_id, loan.member_id, loan.book_id, loan.borrow_date, loan.due_date, loan.returned]
        with open("loans.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        
        updated = []
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["book_id"] == book_id:
                    row["available"] = int(row["available"]) - 1
                updated.append(row)
        with open("books.csv", 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated)
        return f"{loan} Borrow Successfull!!\n"

    def return_book(self):

        loan_id = input("Enter Loan Id: ")
        updated_loans = []
        updated_books = []
        found = False
        with open("loans.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["loan_id"] == loan_id and row["returned"] == "No":
                    row["returned"] = "Yes"
                    target = row["book_id"]
                    found = True
                updated_loans.append(row)
        if found:
            with open("loans.csv", 'w', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_loans)
            with open("books.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                book_field_names = reader.fieldnames
                for row in reader:
                    if row["book_id"] == target:
                        row["available"] = int(row["available"]) + 1
                    updated_books.append(row)
            with open("books.csv", 'w', newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, book_field_names)
                writer.writeheader()
                writer.writerows(updated_books)
            return f"Return Succeffull!!\n"
        else:
            return f"{loan_id} Not found!!\n"

    def view_loan_history(self):
        output = ""
        with open("loans.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Loan Id        : {row["loan_id"]}\n|Member Id      : {row["member_id"]}\n|Book Id        : {row["book_id"]}\n|Borrowed Date  : {row["borrow_date"]}\n|Due Date       : {row["due_date"]}\n|Returned       : {row["returned"]}\n\n"

        return output   
    
    def over_due_loans(self):
        output = ""
        today = date.today()
        exist = False
        with open("loans.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                due_date = date.fromisoformat(row["due_date"])
                if due_date < today and row["returned"] == "No":
                    exist = True
                    output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^\n|Loan Id        : {row["loan_id"]}\n|Member Id      : {row["member_id"]}\n|Book Id        : {row["book_id"]}\n|Borrowed Date  : {row["borrow_date"]}\n|Due Date       : {row["due_date"]}\n|Returned       : {row["returned"]}\n\n"
        if not exist:
            return f"Not one!!\n"
        return output
