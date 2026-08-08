from exceptions import InvalidNameError, InvalidISBNError, InvalidYearError, InvalidTitleError, InvalidCopiesError

class Book:

    def __init__(self, book_id, title, author, category, publication_year, isbn, copies, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.publication_year = publication_year
        self.isbn = isbn
        self.copies = copies
        self.available = available
    
    @property
    def book_id(self):
        return self.__book_id
    
    @book_id.setter
    def book_id(self, book_id):
        self.__book_id = book_id
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if not title.strip() or len(title) >= 150:
            raise InvalidTitleError(title)
        self.__title = title
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        for char in author:
            if not ((char in [" ", "."]) or char.isalpha()):
                raise InvalidNameError(author)
        self.__author = author
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, category):
        if not category.strip():
            raise InvalidNameError(category)

        for char in category:
            if not (char.isalpha() or char == " "):
                raise InvalidNameError(category)
        self.__category = category
    
    @property
    def isbn(self):
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        if not (isbn.isdigit() and len(isbn) == 13):
            raise InvalidISBNError(isbn)
        self.__isbn = isbn
    
    @property
    def publication_year(self):
        return self.__publication_year
    
    @publication_year.setter
    def publication_year(self, publication_year):
        if not (publication_year.isdigit() and len(publication_year) == 4):
            raise InvalidYearError(publication_year)
        self.__publication_year = publication_year
    
    @property
    def copies(self):
        return self.__copies
    
    @copies.setter
    def copies(self, copies):
        if not copies.isdigit():
            raise InvalidCopiesError(copies)
        self.__copies = copies
    
    @property
    def available(self):
        return self.__available
    
    @available.setter
    def available(self, available):
        self.__available = available

    def __str__(self):
        return f"Book ID         :  {self.__book_id}\nTitle           :  {self.__title}\nAuthor          :  {self.__author}\nCategory        :  {self.__category}\nISBN            :  {self.__isbn}\nPublication Year:  {self.__publication_year}\nCopies          :  {self.__copies}\nAvailable       :  {self.__available}"
