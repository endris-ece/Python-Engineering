from models.transaction import Transaction
from utilities.random_generator import RandomGenerator
from services.supplier_manager import SupplierManager
from enum import Enum
from datetime import date
from exceptions import InvalidQuantityError, SupplierNotFoundError, InsufficientQuantityError, ProductNotFoundError
import csv

supplier_manager = SupplierManager()
random_generator = RandomGenerator()
class TransactionType(Enum):
    IN = 1
    OUT = 2

class InventoryManager:

    def stock_in(self):

        updated_products = []
        while True:
            try:
                supplier_found = False
                product_found = False
                product_id = input("Enter product ID: ")
                with open("products.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["product_id"] == product_id:
                            product_found = True
                if not product_found:        
                    raise ProductNotFoundError("Product is not found!!\n")

                print("Is supplier New??\n1. Yes\n2. No\n")
                choice = int(input("Choose: "))
                if choice not in (1, 2):
                    raise ValueError("Choose either 1 or 2.")
                if choice == 1:
                    supplier = supplier_manager.add_supplier()
                    supplier_id = supplier.supplier_id
                elif choice == 2:   
                    supplier_id = input("Enter Supplier id: ")
                    with open("suppliers.csv", 'r', encoding="utf-8") as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row["supplier_id"] == supplier_id:
                                supplier_found = True
                    if not supplier_found:
                        raise SupplierNotFoundError("Supplier is not found!!\n")
                transaction_id = random_generator.generate_transaction_id()
                transaction_type = TransactionType.IN.name
                quantity = int(input("Enter Quantity: "))
                stock_in_date = date.today()
                transaction = Transaction(transaction_id, product_id, supplier_id, transaction_type, quantity, stock_in_date)
                break
            except ProductNotFoundError as e:
                print(e)
            except SupplierNotFoundError as e:
                print(e)
            except InvalidQuantityError as e:
                print(e)
        
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["product_id"] == product_id:
                    product_found = True
                    row["quantity"] = int(row["quantity"]) + int(transaction.quantity)
                updated_products.append(row)
        
        with open("products.csv", 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated_products)
            
        row = [transaction.transaction_id, transaction.product_id, transaction.supplier_id, transaction.transaction_type, transaction.quantity, transaction.date]
        with open("transactions.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        if product_found:
            return f"Stock In successful!!\n\n{transaction}\n"
        return f"Product Not Found!!\n"



        
    def stock_out(self):
        updated_products = []
        while True:
            try:
                product_found = False
                supplier_id = ""
                product_id = input("Enter product ID: ")
                transaction_id = random_generator.generate_transaction_id()
                transaction_type = TransactionType.OUT.name
                quantity = int(input("Enter Quantity: "))
                with open("products.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["product_id"] == product_id:
                            product_found = True
                            if int(row["quantity"]) < quantity:
                                raise InsufficientQuantityError("There is Not enough quantity!!\n")

                if not product_found:
                    raise ProductNotFoundError("Product id is not found!!\n")
                stock_out_date = date.today()
                transaction = Transaction(transaction_id, product_id,"None", transaction_type, quantity, stock_out_date)
                break
            except ProductNotFoundError as e:
                print(e)
            except InsufficientQuantityError as e:
                print(e)
            except SupplierNotFoundError as e:
                print(e)
            except InvalidQuantityError as e:
                print(e)
        
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["product_id"] == product_id:
                    row["quantity"] = int(row["quantity"]) - int(transaction.quantity)
                updated_products.append(row)
        
        with open("products.csv", 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated_products)
            
        row = [transaction.transaction_id, transaction.product_id, transaction.transaction_type, transaction.quantity, transaction.date]
        with open("transactions.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        return f"Stock Out successful!!\n\n{transaction}\n"


    def stock_adjustment(self):
        found = False
        updated_product = []
        while True:
            try:
                product_id = input("Enter product ID: ")
                with open("products.csv", 'r', encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    field_names = reader.fieldnames
                    for row in reader:
                        if row["product_id"] == product_id:
                            quantity = int(input("Enter the correct Quantity: "))
                            if quantity < 0:
                                raise InvalidQuantityError("Quantity cannot be negative.")
                            row["quantity"] = quantity
                            found = True
                        updated_product.append(row)
                if not found:
                    raise ProductNotFoundError("Product is not found!!\n")
                break
            except InvalidQuantityError as e:
                print(e)
            except ProductNotFoundError as e:
                print(e)
        with open("products.csv", 'w', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            writer.writerows(updated_product)
        return f"Stock Adjustment Succesful!!\n"

    def view_transactions(self):
        output = ""
        with open("transactions.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Transactions ID      : {row["transaction_id"]}\n|Product ID          : {row["product_id"]}\n|Supplier ID         : {row["supplier_id"]}\n|Transaction Type    : {row["transaction_type"]}\n|Quantity            : {row["quantity"]}\n|Date                : {row["date"]}\n"
        return output