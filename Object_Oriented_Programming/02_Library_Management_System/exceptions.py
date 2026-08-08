class InvalidNameError(Exception):

    def __init__(self, name):
        self.name = name
        super().__init__(f"{name} contains wrong characters!!\n")

class InvalidISBNError(Exception):

    def __init__(self,isbn):
        self.isbn = isbn
        super().__init__(f"{isbn} should be numeric and contain 13 digit!!\n")

class InvalidYearError(Exception):

    def __init__(self, year):
        self.year = year
        super().__init__(f"{year} should be 4 digits and numeric!!\n")

class InvalidCopiesError(Exception):
    def __init__(self, copies):
        self.copies = copies
        super().__init__(
            f"Invalid copies '{copies}'. Copies must be an integer.\n"
        )

class InvalidPhoneNumberError(Exception):
    def __init__(self, phone_number):
        self.phone_number = phone_number
        super().__init__(
            f"Phone number '{phone_number}' is invalid. "
            f"It must be exactly 10 numeric digits long and start with 0."
        )
class InvalidEmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(
            f"Email '{email}' is invalid.\nIt must contain the '@' symbol And ends with '.com'."
        )

class InvalidTitleError(Exception):
    def __init__(self, title):
        self.title = title
        super().__init__(
            f"Title '{title}' is invalid.\nIt must be less than 150 characters and must not be empty!!!\n"
        )
class InvalidDateError(Exception):
    def __init__(self, date):
        self.date = date
        super().__init__(
            f"Date {date} is invalid!!\n"
        )
class MemberNotFoundError(Exception):
    def __init__(self, member_id):
        self.member_id = member_id
        super().__init__(
            f"Member_id {member_id} is not found!!\n"
        )

class BookNotFoundError(Exception):
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(
            f"Book Id {book_id} is not found!!\n"
        )
class BookNotAvailableError(Exception):
    def __init__(self):
        super().__init__(
            f"There is no available book!!\n"
        )