from exceptions import InvalidProductNameError,InvalidPriceError,InvalidQuantityError,SupplierNotFoundError
from models.product import Product
from utilities.random_generator import RandomGenerator
from enum import Enum
import csv


class Category(Enum):
    ELECTRONICS = 1
    ELECTRICAL_COMPONENTS = 2
    COMPUTER_HARDWARE = 3
    COMPUTER_ACCESSORIES = 4
    MOBILE_ACCESSORIES = 5
    NETWORKING = 6
    TOOLS = 7
    TEST_EQUIPMENT = 8
    CABLES = 9
    POWER_SUPPLIES = 10
    BATTERIES = 11
    OFFICE_SUPPLIES = 12
    STORAGE = 13
    AUDIO_VIDEO = 14
    HOME_APPLIANCES = 15
    SAFETY_EQUIPMENT = 16
    MECHANICAL_PARTS = 17
    SOFTWARE = 18
    OTHER = 19

random_generator =RandomGenerator()

class ProductManager:

    def select_category(self):
        while True:
            try:
                for category in Category:
                    print(f"{category.value}. {category.name}\n")
                
                category = int(input("Selet a category: "))
                if category in [c.value for c in Category]:
                    return Category(category)
                raise ValueError
            except ValueError:
                print("Invalid Input!!\n")


    def add_product(self):
        while True:
            try:
                found = False
                product_id = random_generator.generate_product_id()
                name = input("Enter Product Name: ")
                category = self.select_category().name
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                minimum_stock_level = int(input("Enter minimum_stock_level: "))
                product = Product(product_id, name, category, price, quantity, minimum_stock_level)
                break
            except ValueError:
                print("Price, quantity and minimum stock must be numeric.")
            except InvalidPriceError as e:
                print(e)
            except InvalidProductNameError as e:
                print(e)
            except InvalidQuantityError as e:
                print(e)
        row = [product.product_id, product.name, product.category, product.price, product.quantity, product.minimum_stock_level]
        with open("products.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        return product

    def view_products(self):
        output = ""
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Product ID          : {row["product_id"]}\n|Product Name        : {row["name"]}\n||Category            : {row["category"]}\n|Price               : {row["price"]}\n|Quantity            : {row["quantity"]}\n|Minimum Stock Level : {row["minimum_stock_level"]}\n\n"
        return output

    def search_product(self):
        product_id = input("Enter Product ID: ")
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if product_id == row["product_id"]:
                    return f"Product is Found!!\n|Product ID          : {row["product_id"]}\n|Product Name        : {row["name"]}\n||Category            : {row["category"]}\n|Price               : {row["price"]}\n|Quantity            : {row["quantity"]}\n|Minimum Stock Level : {row["minimum_stock_level"]}\n\n"
        return f"Product not found!!\n"

    def update_product(self):

        updated_list = []
        def select_option():
            while True:
                try:
                    print("\n1. Update Name")
                    print("2. Update Category")
                    print("3. Update Price")
                    print("4. Update Minimum Stock")
                    print("5. Exit")
                    option = int(input("Choose your option: "))
                    if option in range(1,6):
                        return option
                    raise ValueError
                except ValueError:
                    print("Choose from 1 to 5\n")

        target = input("Enter the product's ID you want to update: ")
        found = False
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["product_id"] == target:
                    found = True
                    while True:
                        try:
                            option = select_option()

                            if option == 1:
                                name = input("Enter the correct Name: ")
                                Product(
                                    row["product_id"],
                                    name,
                                    row["category"],
                                    float(row["price"]),
                                    int(row["quantity"]),
                                    int(row["minimum_stock_level"])
                                )
                                row["name"] = name

                            elif option == 2:
                                category = self.select_category().name
                                row["category"] = category

                            elif option == 3:
                                price = float(input("Enter the correct Price: "))
                                Product(
                                    row["product_id"],
                                    row["name"],
                                    row["category"],
                                    price,
                                    int(row["quantity"]),
                                    int(row["minimum_stock_level"])
                                )
                                row["price"] = price

                            elif option == 4:
                                minimum_stock = int(input("Enter the correct Minimum Stock: "))
                                Product(
                                    row["product_id"],
                                    row["name"],
                                    row["category"],
                                    float(row["price"]),
                                    int(row["quantity"]),
                                    minimum_stock
                                )
                                row["minimum_stock_level"] = minimum_stock

                            elif option == 5:
                                break

                        except ValueError:
                            print("Invalid numeric input!")
                        except InvalidPriceError as e:
                            print(e)
                        except InvalidProductNameError as e:
                            print(e)
                        except InvalidQuantityError as e:
                            print(e)

                    updated_product = Product(
                        row["product_id"],
                        row["name"],
                        row["category"],
                        float(row["price"]),
                        int(row["quantity"]),
                        int(row["minimum_stock_level"])
                    )
                updated_list.append(row)
        if found:
            with open("products.csv", 'w', newline="",encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_list)
            return updated_product
        else:
            return f"Not Found!!\n"
    
    def delete_product(self):
        target = input("Enter product id you want to delete: ")
        updated_list = []
        found = False
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["product_id"] == target:
                    found = True
                    continue
                updated_list.append(row)
        if not found:
            return f"Target Not found!!\n"
        else:
            with open("products.csv", 'w', newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_list)
            return f"Deletion succesful!!\n"

    def inventory_report(self):
        output = ""
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Product ID          : {row["product_id"]}\n|Product Name        : {row["name"]}\n||Category            : {row["category"]}\n|Price               : {row["price"]}\n|Quantity            : {row["quantity"]}\n|Minimum Stock Level : {row["minimum_stock_level"]}\n|Inventory Value      : {float(row["price"])*(int(row["quantity"]))}\n\n"
        return output

    def inventory_value(self):
        value = 0
        output = ""
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}{row["name"]}               : {int(row["quantity"])*float(row["price"])}\n"
                value = value + int(row["quantity"])*float(row["price"])
        return f"Product Name               Value\n{output}------------------------\nTotal              : {value}\n"


    def inventory_summary(self):
        total_products = 0
        total_units = 0
        total_suppliers = 0
        low_stock_products = 0
        out_of_stock = 0
        inventory_value = 0

        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_products += 1
                total_units += int(row["quantity"])
                if int(row["quantity"]) <= int(row["minimum_stock_level"]):
                    low_stock_products += 1
                if int(row["quantity"]) == 0:
                    out_of_stock += 1
                inventory_value += (int(row["quantity"])*float(row["price"]))
        with open("suppliers.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                total_suppliers += 1
        
        return f"Total Products      : {total_products}\nTotal Units         : {total_units}\nTotal Suppliers     : {total_suppliers}\nLow Stock           : {low_stock_products}\nOut of Stock        : {out_of_stock}\nInventory Value     : {inventory_value}"

    def check_low_stock(self):
        output = ""
        with open("products.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row["quantity"]) <= int(row["minimum_stock_level"]):
                    output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Product ID          : {row["product_id"]}\n|Product Name        : {row["name"]}\n||Category            : {row["category"]}\n|Price               : {row["price"]}\n|Quantity            : {row["quantity"]}\n|Minimum Stock Level : {row["minimum_stock_level"]}\n\n"
        return output
    