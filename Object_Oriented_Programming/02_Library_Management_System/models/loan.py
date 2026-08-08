
class Loan:

    def __init__(self, loan_id, member_id, book_id, borrow_date, due_date, returned):
        self.loan_id = loan_id
        self.member_id = member_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.returned = returned

    @property
    def loan_id(self):
        return self.__loan_id
    
    @property
    def member_id(self):
        return self.__member_id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def returned(self):
        return self.__returned

    @loan_id.setter
    def loan_id(self, loan_id):
        self.__loan_id = loan_id
    
    @member_id.setter
    def member_id(self, member_id):
        self.__member_id = member_id
    
    @book_id.setter
    def book_id(self, book_id):
        self.__book_id = book_id

    @borrow_date.setter
    def borrow_date(self, borrow_date):
        self.__borrow_date = borrow_date
    
    @due_date.setter
    def due_date(self, due_date):
        self.__due_date = due_date
    
    @returned.setter
    def returned(self, returned):
        self.__returned = returned

    def __str__(self):
        return f"Loan ID         :  {self.__loan_id}\nBook ID         :  {self.__book_id}\nMember ID       :  {self.__member_id}\nBorrow Date     :  {self.__borrow_date}\nDue Date         :  {self.__due_date}\nReturned         :  {self.__returned}\n"
