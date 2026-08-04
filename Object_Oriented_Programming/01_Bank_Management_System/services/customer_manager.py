from models.customer import Customer
from utilities.random_generator import RandomGenerator
import csv

class CustomerManager:

    def create_customer(self):
        random_generator = RandomGenerator()
        first_name = input("Enter your firt name: ")
        second_name = input("Enter your second name: ")
        phone_number = input("Enter your phone number: ")
        email = input("Enter your Email: ")
        address = input("Enter your address: ")
        custom_id = random_generator.generate_ID()
        customer = Customer(custom_id, first_name, second_name, phone_number, email, address)
        
        customer_row = [customer.c_ID, customer.f_name, customer.s_name, customer.phone, customer.email, customer.address]
        with open("customers.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(customer_row)
        
        return customer
    
    def view_customers(self):

        output = ""
        with open("customers.csv", 'r', encoding="utf-8")as file:
            reader = csv.DictReader(file)
            output = f"{reader.fieldnames}"
            for row in reader:
                output = f"{output}\n{row["customer_Id"]}   |   {row["first_name"]}   |   {row["second_name"]}   |   {row["phone_number"]}   |   {row["email"]}   |   {row["address"]}\n"

        return f"operation successful!!!\n{output}"

    def enter_ID(self):
        custom_ID = input("Enter customer id: ")
        return custom_ID

    def search_customer(self):
        customer_id = self.enter_ID()
        with open("customers.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["customer_Id"] == customer_id:
                    return f"Found!\n{row}"
            
            return f"Not Found!!"

    def delete_customer(self):
        customer_id = self.enter_ID()
        ramaining_row = []
        with open("customers.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["customer_Id"] != customer_id:
                    ramaining_row.append(row)
                
        with open("customers.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(ramaining_row)

        return f"Customer {customer_id} deleted successfully!"

    def update_customer(self):
        customer_id = self.enter_ID()
        found = False
        updated = []
        with open("customers.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["customer_Id"] == customer_id:
                    found = True
                    f_name = row["first_name"]
                    s_name = row["second_name"]
                    phone = "0"
                    for i in range(len(row["phone_number"])):
                        if i > 4:
                            phone = f"{phone}{row["phone_number"][i]}"
                    email = row["email"]
                    address = row["address"]
                    while True:
                        try:
                            target = int(input("What do you want to update:\n1. First Name\n2. Second Name\n3. Phone number\n4. email\n5. address\n: "))
                            
                            if target == 1:
                                f_name = input("Enter customer's first name: ")
                            
                            elif target == 2:
                                s_name = input("Enter your second name: ")

                            elif target == 3:
                                phone = input("Enter your phone number: ")

                            elif target == 4:
                                email = input("Enter your email: ")
                            
                            elif target == 5:
                                address = input("Enter your address: ")

                            else:
                                raise ValueError

                            updated_customer = Customer(customer_id, f_name, s_name, phone, email, address)
                            row["first_name"] = updated_customer.f_name
                            row["second_name"] = updated_customer.s_name
                            row["phone_number"] = updated_customer.phone
                            row["email"] = updated_customer.email
                            row["address"] = updated_customer.address
                            break
                        except ValueError:
                            print("please choose from 1 to 5")
                        except Exception as e:
                            print(e)
                updated.append(row)

        with open("customers.csv", 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(updated)
        if found:
            return f"Update successful!!\n{updated_customer}"
        return f"Not Found!!\n"
