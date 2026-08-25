from models.supplier import Supplier
from exceptions import InvalidNameError,InvalidPhoneNumberError,InvalidAddressError,InvalidEmailError
from utilities.random_generator import RandomGenerator
import csv


class SupplierManager:

    def __init__(self):
        self.random_generator = RandomGenerator()

    def add_supplier(self):

        while True:
            try:
                supplier_id = self.random_generator.generate_supplier_id()

                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                phone_number = input("Enter Phone Number: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")

                supplier = Supplier(supplier_id,first_name,last_name,phone_number,email,address)
                break
            except InvalidEmailError as e:
                print(e)
            except InvalidNameError as e:
                print(e)
            except InvalidPhoneNumberError as e:
                print(e)
            except InvalidAddressError as e:
                print(e)
        row = [supplier.supplier_id, supplier.first_name, supplier.last_name, supplier.phone, supplier.email, supplier.address]
        with open("suppliers.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        return supplier

    def view_suppliers(self):

        output = ""
        with open("suppliers.csv","r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output += (
                    "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
                    f'|Supplier Id     : {row["supplier_id"]}\n'
                    f'|Full Name       : {row["first_name"]} '
                    f'{row["last_name"]}\n'
                    f'|Phone Number    : {row["phone"]}\n'
                    f'|Email           : {row["email"]}\n'
                    f'|Address         : {row["address"]}\n\n'
                )
        return output


    def search_supplier(self):

        supplier_id = input("Enter Supplier Id: ")

        with open("suppliers.csv","r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if supplier_id == row["supplier_id"]:
                    return (
                        "Supplier is Found!!\n"
                        f'|Supplier Id     : {row["supplier_id"]}\n'
                        f'|Full Name       : {row["first_name"]} '
                        f'{row["last_name"]}\n'
                        f'|Phone Number    : {row["phone"]}\n'
                        f'|Email           : {row["email"]}\n'
                        f'|Address         : {row["address"]}\n\n'
                    )
        return "Supplier not found!!\n"

    def update_supplier(self):
        updated = False
        target = input("Enter the supplier's Id you want to update: ")
        updated_list = []
        found = False
        with open("suppliers.csv","r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["supplier_id"] == target:
                    found = True
                    while True:
                        print("\n1. Update First Name")
                        print("2. Update Last Name")
                        print("3. Update Phone Number")
                        print("4. Update Email")
                        print("5. Update Address")
                        print("6. Exit")
                        try:
                            option = int(input("Choose your option: "))
                            if option not in range(1, 7):
                                raise ValueError
                        except ValueError:
                            print("Choose from 1 to 6\n")
                            continue
                        if option == 6:
                            break
                        try:
                            first_name = row["first_name"]
                            last_name = row["last_name"]
                            phone = "0" + row["phone"].replace("+251 ", "")
                            email = row["email"]
                            address = row["address"]

                            if option == 1:
                                first_name = input("Enter the correct First Name: ")

                            elif option == 2:
                                last_name = input("Enter the correct Last Name: ")

                            elif option == 3:
                                phone = input("Enter the correct Phone Number: ")

                            elif option == 4:
                                email = input("Enter the correct Email: ")

                            elif option == 5:
                                address = input("Enter the correct Address: ")

                            supplier = Supplier(row["supplier_id"],first_name,last_name,phone,email,address)
                            row["first_name"] = supplier.first_name
                            row["last_name"] = supplier.last_name
                            row["phone"] = supplier.phone
                            row["email"] = supplier.email
                            row["address"] = supplier.address
                            updated = True

                        except InvalidEmailError as e:
                            print(e)
                        except InvalidNameError as e:
                            print(e)
                        except InvalidPhoneNumberError as e:
                            print(e)
                        except InvalidAddressError as e:
                            print(e)
                updated_list.append(row)
        if not found:
            return "Not Found!!\n"

        with open("suppliers.csv","w",newline="",encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(updated_list)
        if updated:
            return "Supplier updated successfully!!\n"
        else:
            return "No changes were made.\n"
            
    def delete_supplier(self):
        target = input("Enter Supplier id you want to delete: ")
        updated_list = []
        found = False
        with open("suppliers.csv","r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["supplier_id"] == target:
                    found = True
                    continue
                updated_list.append(row)
        if not found:
            return "Target Not found!!\n"
        with open("suppliers.csv","w",newline="",encoding="utf-8") as file:
            writer = csv.DictWriter(file,fieldnames=field_names)
            writer.writeheader()
            writer.writerows(updated_list)
        return "Deletion successful!!\n"