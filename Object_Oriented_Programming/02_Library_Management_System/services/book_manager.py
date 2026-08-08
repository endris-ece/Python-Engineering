from models.book import Book
from utilities.random_generator import RandomGenerator
from exceptions import InvalidNameError, InvalidISBNError, InvalidYearError, InvalidTitleError, InvalidCopiesError
import csv

class BookManager:

    def __init__(self):
        self.random_generator = RandomGenerator()

    def add_book(self):
        while True:
            try:
                book_id = self.random_generator.generate_book_id()
                title = input("Enter Book Title: ")
                author = input("Enter the Author: ")
                category = input("Enter Category: ")
                publication_year = input("Enter Publication Year: ")
                isbn = input("Enter ISBN: ")
                with open("books.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["isbn"] == isbn:
                            raise ValueError
                copies = input("Enter number of copies: ")
                available = copies
                book = Book(book_id, title, author, category, publication_year, isbn, copies, available)
                break
            except ValueError:
                print("ISBN already exists!!\n")
            except InvalidTitleError as e:
                print(e)
            except InvalidNameError as e:
                print(e)
            except InvalidISBNError as e:
                print(e)
            except InvalidYearError as e:
                print(e)
        
        row  = [book.book_id, book.title, book.author, book.category, book.publication_year, book.isbn, book.copies, book.available]
        with open("books.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        return f"{book}\nThis book is added successfully!!\n"
    
    def view_books(self):
        output = ""
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Book Id         : {row["book_id"]}\n|Title           : {row["title"]}\n|Author          : {row["author"]}\n|Category        : {row["category"]}\n|Publication Year: {row["publication_year"]}\n|ISBN            : {row["isbn"]}\n|Copies          : {row["copies"]}\n|Available       : {row["available"]}\n\n"
        return output
    
    def search_book(self):
        isbn = input("Enter the books ISBN: ")
        found = False
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if isbn == row["isbn"]:
                    found = True
                    target = row
        if found:
            return f"The book is Found!!\n|Book Id         : {target["book_id"]}\n|Title           : {target["title"]}\n|Author          : {target["author"]}\n|Category        : {target["category"]}\n|Publication Year: {target["publication_year"]}\n|ISBN            : {target["isbn"]}\n|Copies          : {target["copies"]}\n|Available       : {target["available"]}\n"
        else:
            return f"Book not found!!\n"
    
    def update_book(self):
        updated_list = []
        def select_option():
            while True:
                try:
                    print("\n1. Update Title")
                    print("2. Update Author")
                    print("3. Update Category")
                    print("4. Update Publication year")
                    print("5. Update Copies")
                    print("6. Exit")
                    option = int(input("Choose your option: "))
                    if option in range(1,7):
                        return option
                    raise ValueError
                except ValueError:
                    print("Choose from 1 to 6\n")

        target = input("Enter the book's Id you want to update: ")
        found = False
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["book_id"] == target:
                    found = True
                    while True:
                        try:
                            option = select_option()
                            if option == 1:
                                title = input("Enter the correct Title: ")
                                row["title"] = title
                            elif option == 2:
                                author = input("Enter the correct Author: ")
                                row["author"] = author
                            elif option == 3:
                                category = input("Enter the correct Category: ")
                                row["category"] = category
                            elif option == 4:
                                publication_year = input("Enter the correct Publication Year: ")
                                row["publication_year"] = publication_year
                            elif option == 5:
                                copies = input("Enter the correct number of copies: ")

                                if not copies.isdigit():
                                    raise InvalidCopiesError()

                                borrowed = int(row["copies"]) - int(row["available"])

                                copies = int(copies)

                                if copies < borrowed:
                                    raise InvalidCopiesError()

                                row["copies"] = str(copies)
                                row["available"] = str(copies - borrowed)

                            elif option == 6:
                                return f"Exit success!!\n"
                            updated_book = Book(row["book_id"], row["title"], row["author"], row["category"], row["publication_year"], row["isbn"], row["copies"], row["available"])
                            break
                        except InvalidTitleError as e:
                            print(e)
                        except InvalidNameError as e:
                            print(e)
                        except InvalidISBNError as e:
                            print(e)
                        except InvalidYearError as e:
                            print(e)
                        except InvalidCopiesError as e:
                            print(e)
                updated_list.append(row)
        if found:
            with open("books.csv", 'w', newline="",encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_list)
            return updated_book
        else:
            return f"Not Found!!\n"

    def delete_book(self):
        target = input("Enter book id of the book you want to delete: ")
        updated_list = []
        found = False
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["book_id"] == target:
                    found = True
                    continue
                updated_list.append(row)
        if not found:
            return f"Target Not found!!\n"
        else:
            with open("loans.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["book_id"] == target:
                        return f"This Book Exists In Borrow Lists!!\n"
                        
            with open("books.csv", 'w', newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_list)
            return f"Deletion succesful!!\n"

    def view_available_books(self):
        output = ""
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["available"]) >= 1:
                    output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Book Id         : {row["book_id"]}\n|Title           : {row["title"]}\n|Author          : {row["author"]}\n|Category        : {row["category"]}\n|Publication Year: {row["publication_year"]}\n|ISBN            : {row["isbn"]}\n|Copies          : {row["copies"]}\n|Available       : {row["available"]}\n\n"
        return output

    def borrowed_books(self):
        output = ""
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["copies"]) > int(row["available"]):
                    output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Book Id         : {row["book_id"]}\n|Title           : {row["title"]}\n|Author          : {row["author"]}\n|Category        : {row["category"]}\n|Publication Year: {row["publication_year"]}\n|ISBN            : {row["isbn"]}\n|Copies          : {row["copies"]}\n|Available       : {row["available"]}\n\n"
        return output

    def total_books(self):
        books = 0
        with open("books.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books += 1
        return f"Total Books = {books}\n"