# Inventory Management System

A console-based Inventory Management System developed in Python using Object-Oriented Programming (OOP) principles.

The system manages products, suppliers, inventory stock, and transaction records using CSV files for persistent data storage.

## Features

### 1. Product Management

* Add new products
* View all products
* Search products by product ID
* Update product information
* Delete products
* Categorize products
* Set minimum stock levels
* Validate product names, prices, quantities, and stock levels

### 2. Supplier Management

* Add suppliers
* View all suppliers
* Search suppliers
* Update supplier information
* Delete suppliers
* Validate:

  * Names
  * Phone numbers
  * Email addresses
  * Addresses

### 3. Stock Management

* Stock in
* Stock out
* Stock adjustment
* Associate suppliers with stock-in transactions
* Track transaction IDs
* Track transaction dates
* Prevent stock-out operations when available quantity is insufficient
* Validate product and supplier existence

### 4. Reports

* Inventory report
* Low-stock product report
* Transaction records
* Inventory value
* Inventory summary
* Total products
* Total units
* Total suppliers
* Low-stock products
* Out-of-stock products

## Technologies

* **Python**
* Object-Oriented Programming
* CSV file handling
* Python `enum`
* Exception handling
* File I/O

## Project Structure

03_Inventory_Management_System/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── product.py
│   ├── supplier.py
│   └── transaction.py
│
├── services/
│   ├── __init__.py
│   ├── product_manager.py
│   ├── supplier_manager.py
│   └── inventory_manager.py
│
├── utilities/
│   ├── __init__.py
│   ├── random_generator.py
│
│
├── exceptions.py
│
├── products.csv
├── suppliers.csv
└── transactions.csv

## Data Storage

The application uses CSV files instead of a database.

### `products.csv`

Stores information such as:

* Product ID
* Product name
* Category
* Price
* Quantity
* Minimum stock level

### `suppliers.csv`

Stores:

* Supplier ID
* First name
* Last name
* Phone number
* Email
* Address

### `transactions.csv`

Stores inventory movement records such as:

* Transaction ID
* Product ID
* Supplier ID
* Transaction type
* Quantity
* Date

## OOP Concepts Used

This project was built to practice practical Object-Oriented Programming concepts.

### Classes and Objects

The system uses separate classes for different entities:

* `Product`
* `Supplier`
* `Transaction`
* `ProductManager`
* `SupplierManager`
* `InventoryManager`

### Encapsulation

Private attributes and properties are used to control access to object data.

Example:

@property
def price(self):
    return self.__price

Validation is performed through property setters.

### Exception Handling

Custom exceptions are used to handle invalid input and business rules.

Examples include:

InvalidProductNameError
InvalidPriceError
InvalidQuantityError
InvalidNameError
InvalidPhoneNumberError
InvalidEmailError
InvalidAddressError
ProductNotFoundError
SupplierNotFoundError
InsufficientQuantityError


### Enumerations

Python `Enum` is used for predefined categories and transaction types.

Example:

```python
class TransactionType(Enum):
    IN = 1
    OUT = 2
```

### Composition

Manager classes work with model classes to perform operations on the corresponding entities.

## Running the Project

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd Python-Engineering/Object_Oriented_Programming/03_Inventory_Management_System
```

Run:

```bash
python main.py
```

The application provides a menu-driven console interface.

## Example Main Menu

===============================================
        INVENTORY MANAGEMENT SYSTEM
===============================================

1. Product Management
2. Supplier Management
3. Stock Management
4. Reports
5. Exit

## Validation

The system validates data before modifying the CSV files.

For example:

* Product price must be numeric and greater than zero.
* Product quantity must be a non-negative integer.
* Minimum stock level must be a non-negative integer.
* Supplier phone numbers must follow the expected format.
* Supplier email addresses must be valid.
* Stock-out quantity cannot exceed available inventory.
* Products and suppliers must exist when required.

## Design Approach

Products and suppliers are maintained independently.

A product does **not** contain a permanent supplier ID because the same product can be supplied by multiple suppliers.

Instead, supplier information is associated with inventory transactions, particularly stock-in operations.

This allows the system to represent situations such as:

Supplier A → supplies → Capacitor
Supplier B → supplies → Capacitor
Supplier C → supplies → Capacitor


while keeping `Product` independent of any particular supplier.

## Purpose

This project was developed as part of my Python programming and Object-Oriented Programming practice.

The main goals are to:

* Strengthen Python OOP skills
* Practice class design
* Practice encapsulation and validation
* Work with custom exceptions
* Practice CSV-based data persistence
* Build a multi-module Python application
* Practice designing relationships between different entities
* Develop a larger console-based application from scratch

## Future Improvements

Possible future improvements include:

* Database integration
* Improved transaction history
* Supplier-product relationship reports
* Automatic low-stock notifications
* User authentication and roles
* Better formatted console interface
* Unit tests
* Automated test suite
* Logging
* GUI or web interface

## Author

**Endris Mohammed**

Electrical & Computer Engineering Student

This project is part of my engineering programming portfolio, documenting my progress in Python, Object-Oriented Programming, and practical software development.
