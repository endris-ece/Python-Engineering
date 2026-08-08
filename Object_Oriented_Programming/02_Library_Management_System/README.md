# Library Management System

A console-based Library Management System developed in Python using Object-Oriented Programming (OOP).

The system manages books, library members, and borrowing/returning operations while storing persistent data in CSV files.

## Features

### Book Management

* Add new books
* View all books
* Search books by ISBN
* Update book information
* Delete books
* View available books
* View borrowed books
* Track total books and available copies
* Prevent duplicate ISBNs

### Member Management

* Register new members
* View all members
* Search members
* Update member information
* Remove members
* Track total registered members
* Validate names, phone numbers, email addresses, and addresses

### Borrowing & Returning

* Borrow books
* Return books
* Automatically decrease available copies when a book is borrowed
* Automatically increase available copies when a book is returned
* Generate loan IDs
* Generate borrowing and due dates
* Track whether a loan has been returned
* Prevent borrowing unavailable books
* Validate members and books before creating loans

### Reports

* View available books
* View borrowed books
* View loan history
* View overdue loans
* View library summary

## Project Structure

02_Library_Management_System/
│
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   └── loan.py
│
├── services/
│   ├── __init__.py
│   ├── book_manager.py
│   ├── member_manager.py
│   └── loan_manager.py
│
├── utilities/
│   ├── __init__.py
│   └── random_generator.py
│
├── __init__.py
├── exceptions.py
├── books.csv
├── members.csv
├── loans.csv
├── main.py
└── README.md

## OOP Design

The project is organized into separate layers.

### Models

The `models` package contains the main entities of the system:

* `Book` — represents a library book and its copies.
* `Member` — represents a registered library member.
* `Loan` — represents a borrowing transaction.

### Services

The `services` package contains the operations performed on the models:

* `BookManager` — handles book operations.
* `MemberManager` — handles member operations.
* `LoanManager` — handles borrowing and returning books.

### Utilities

The `utilities` package contains reusable functionality such as ID generation.

### Custom Exceptions

`exceptions.py` contains custom exceptions used for input validation and business rules, including:

* `InvalidNameError`
* `InvalidISBNError`
* `InvalidYearError`
* `InvalidCopiesError`
* `InvalidPhoneNumberError`
* `InvalidEmailError`
* `InvalidTitleError`
* `InvalidDateError`
* `MemberNotFoundError`
* `BookNotFoundError`
* `BookNotAvailableError`

## Data Storage

The system uses CSV files for persistent storage instead of a database.

books.csv
members.csv
loans.csv

This allows data to remain available after the program is closed while keeping the project focused on Python OOP and file handling.

## Technologies Used

* Python
* Object-Oriented Programming
* Classes and Objects
* Encapsulation
* Properties and Setters
* Inheritance through custom exceptions
* Enumerations (`Enum`)
* CSV file handling
* File I/O
* Exception handling
* Date handling
* Modular programming

## How to Run

Clone the repository and navigate to the project directory:

bash
cd 02_Library_Management_System


Run the program:

bash
python main.py

The main menu provides access to:

1. Book Management
2. Member Management
3. Borrow & Return
4. Reports
5. Exit

## Learning Objectives

This project was developed to practice applying Python OOP concepts to a larger, multi-module application.

The main objectives were to:

* Design classes representing real-world entities
* Apply encapsulation using properties
* Separate models from business logic
* Organize a Python project into packages and modules
* Work with CSV files for persistent data
* Implement custom exceptions
* Validate user input
* Use `Enum` for menu and operation selection
* Manage relationships between books, members, and loans
* Build a complete console-based application

## Author

**Endris Mohammed**

Electrical & Computer Engineering Student
