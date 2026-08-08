from services.book_manager import BookManager
from services.member_manager import MemberManager
from services.loan_manager import LoanManager
from enum import Enum

class OPTION(Enum):
    BOOK_MANAGEMENT = 1
    MEMBER_MANAGEMENT = 2
    TRANSACTION = 3
    REPORTS = 4

class BOOK(Enum):
    ADD_BOOK = 1
    VIEW_BOOKS = 2
    SEARCH_BOOK = 3
    UPDATE_BOOK = 4
    DELETE_BOOK = 5

class MEMBER(Enum):
    REGISTER_MEMBER = 1
    VIEW_MEMBERS = 2
    SEARCH_MEMBER = 3
    UPDATE_MEMBER = 4
    REMOVE_MEMBER = 5

class TRANSACTION(Enum):
    BORROW = 1
    RETURN = 2

class REPORTS(Enum):
    AVAILABLE_BOOKS = 1
    BORROWED_BOOKS = 2
    LOAN_HISTORY = 3
    OVER_DUE_LOANS = 4
    SUMMARY = 5
    
book_manager = BookManager()
member_manager = MemberManager()
loan_manager = LoanManager()

def book_management():
    
    def select_option():
        while True:
            try:
                print("*************************************")
                print("\tBOOK MANAGEMENT")
                print("*************************************")
                print("1. Add Book")
                print("2. View All Books")
                print("3. Search Book")
                print("4. Update Book")
                print("5. Delete Book")
                print("6. Exit")
                option = int(input("Select an option: "))
                
                if option in range(1,7):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input!! Value should be in (1, 6)\n")
    
    operations = {
        BOOK.ADD_BOOK: book_manager.add_book,
        BOOK.VIEW_BOOKS: book_manager.view_books,
        BOOK.SEARCH_BOOK: book_manager.search_book,
        BOOK.UPDATE_BOOK: book_manager.update_book,
        BOOK.DELETE_BOOK: book_manager.delete_book
    }
    option = select_option()
    while option != 6:
        print(operations[BOOK(option)]())
        option = select_option()

def member_management():
    
    def select_option():
        while True:
            try:
                print("*************************************")
                print("\tMEMBER MANAGEMENT")
                print("*************************************")
                print("1. Register Member")
                print("2. View Members")
                print("3. Search Member")
                print("4. Update Member")
                print("5. Remove Member")
                print("6. Exit")
                option = int(input("Select an option: "))
                
                if option in range(1,7):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input!! Value should be in (1, 6)\n")
    operations = {
        MEMBER.REGISTER_MEMBER: member_manager.register_member,
        MEMBER.VIEW_MEMBERS: member_manager.view_members,
        MEMBER.SEARCH_MEMBER: member_manager.search_member,
        MEMBER.UPDATE_MEMBER: member_manager.update_member,
        MEMBER.REMOVE_MEMBER: member_manager.remove_member
    }

    option = select_option()
    while option != 6:
        print(operations[MEMBER(option)]())
        option = select_option()
        
def transaction():

    def select_option():
        while True:
            try:
                print("*************************************")
                print("\tTransaction MANAGEMENT")
                print("*************************************")
                print("1. Borrow Book")
                print("2. Return Book")
                print("3. Exit")
                option = int(input("Select an option: "))
                
                if option in range(1,4):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input!! Value should be in (1, 3)\n")

    operations = {
        TRANSACTION.BORROW: loan_manager.borrow_book,
        TRANSACTION.RETURN: loan_manager.return_book
    }

    option = select_option()
    while option != 3:
        print(operations[TRANSACTION(option)]())
        option = select_option()

        
def reports():
    def select_option():
        while True:
            try:
                print("===============================================")
                print("\tReports MANAGEMENT")
                print("===============================================")
                print("1. View Available Books")
                print("2. View Borrowed Books")
                print("3. View Loan History")
                print("4. View Over Due Loans")
                print("5. Library Summary")
                print("6. Exit")
                option = int(input("Select an option: "))
                if option in range(1,7):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input! Value should be in(1,6).\n")
    def summary():
        return f"{member_manager.total_members()}{book_manager.total_books()}"
 
    operations = {
        REPORTS.AVAILABLE_BOOKS: book_manager.view_available_books,
        REPORTS.BORROWED_BOOKS: book_manager.borrowed_books,
        REPORTS.LOAN_HISTORY: loan_manager.view_loan_history,
        REPORTS.OVER_DUE_LOANS: loan_manager.over_due_loans,
        REPORTS.SUMMARY: summary
    }

    option = select_option()
    while option != 6:
        print(operations[REPORTS(option)]())
        option = select_option()
                

def start():

    def select_option():
        while True:
            try:
                print("===============================================")
                print("\tLIBRARY MANAGEMENT")
                print("===============================================")
                print("1. Book Management")
                print("2. Member Management")
                print("3. Borrow & Return")
                print("4. Reports")
                print("5. Exit")
                option = int(input("Select an option: "))
                if option in range(1,6):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input! Value should be in(1,5).\n")

    operations = {
        OPTION.BOOK_MANAGEMENT: book_management,
        OPTION.MEMBER_MANAGEMENT: member_management,
        OPTION.TRANSACTION: transaction,
        OPTION.REPORTS: reports

    }

    option = select_option()
    while option != 5:
        operations[OPTION(option)]()
        option = select_option()

start()
