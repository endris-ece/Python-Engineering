from models.member import Member
from utilities.random_generator import RandomGenerator
from exceptions import InvalidEmailError, InvalidNameError, InvalidPhoneNumberError
from datetime import date
import csv

class MemberManager:
    
    def __init__(self):
        self.random_generator = RandomGenerator()
    
    def register_member(self):
        while True:
            try:
                member_id = self.random_generator.generate_member_id()
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                phone_number = input("Enter Phone Number: ")
                email = input("Enter Email: ")
                address = input("Enter Address: ")
                registration_date = date.today()
                member = Member(member_id, first_name, last_name, phone_number, email, address, registration_date)
                break
            except InvalidEmailError as e:
                print(e)
            except InvalidNameError as e:
                print(e)
            except InvalidPhoneNumberError as e:
                print(e)
        row  = [member.member_id, member.first_name, member.last_name, member.phone_number, member.email, member.address, member.registration_date]
        with open("members.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)

        return f"{member}\nThis member is registered successfully!!\n"
    
    def view_members(self):
        output = ""
        with open("members.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                output = f"{output}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n|Member Id       : {row["member_id"]}\n|Full Name       : {row["first_name"]} {row["last_name"]}\n|Phone Number    : {row["phone_number"]}\n|Email           : {row["email"]}\n|Address         : {row["address"]}\n|Registration Date: {row["registration_date"]}\n\n"
        return output
    
    def search_member(self):
        member_id = input("Enter Member Id: ")
        found = False
        with open("members.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if member_id == row["member_id"]:
                    found = True
                    target = row
        if found:
            return f"Member is Found!!\n|Member Id       : {target["member_id"]}\n|Full Name       : {target["first_name"]} {target["last_name"]}\n|Phone Number    : {target["phone_number"]}\n|Email           : {target["email"]}\n|Address         : {target["address"]}\n|Registration Date: {target["registration_date"]}\n"
        else:
            return f"Member not found!!\n"
    
    def update_member(self):
        updated_list = []
        def select_option():
            while True:
                try:
                    print("\n1. Update First Name")
                    print("2. Update Last Name")
                    print("3. Update Phone Number")
                    print("4. Update Email")
                    print("5. Update Address")
                    print("6. Exit")
                    option = int(input("Choose your option: "))
                    if option in range(1,7):
                        return option
                    raise ValueError
                except ValueError:
                    print("Choose from 1 to 6\n")

        target = input("Enter the members's Id you want to update: ")
        found = False
        with open("members.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["member_id"] == target:
                    row["phone_number"] = f"0{row["phone_number"][5:]}"
                    found = True
                    while True:
                        try:
                            option = select_option()
                            if option == 1:
                                first_name = input("Enter the correct First Name: ")
                                row["first_name"] = first_name
                            elif option == 2:
                                last_name = input("Enter the correct Last Name: ")
                                row["last_name"] = last_name
                            elif option == 3:
                                phone_number = input("Enter the correct Phone Number: ")
                                row["phone_number"] = phone_number
                            elif option == 4:
                                email = input("Enter the correct Email: ")
                                row["email"] = email
                            elif option == 5:
                                address = input("Enter the correct Address: ")
                                row["address"] = address
                            elif option == 6:
                                return f"Exit success!!\n"
                            updated_member = Member(row["member_id"], row["first_name"], row["last_name"], row["phone_number"], row["email"], row["address"], row["registration_date"])
                            row["phone_number"] = updated_member.phone_number
                            break
                        except InvalidEmailError as e:
                            print(e)
                        except InvalidNameError as e:
                            print(e)
                        except InvalidPhoneNumberError as e:
                            print(e)
                updated_list.append(row)

        if found:
            with open("members.csv", 'w', newline="",encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_list)
            return updated_member
        else:
            return f"Not Found!!\n"


    def remove_member(self):
        target = input("Enter Member id you want to delete: ")
        updated_list = []
        found = False
        with open("members.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_name = reader.fieldnames
            for row in reader:
                if row["member_id"] == target:
                    found = True
                    continue
                updated_list.append(row)
        if not found:
            return f"Target Not found!!\n"
        else:
            with open("loans.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["member_id"] == target:
                        return f"This Member Exists In Borrow Lists!!\n"
                        
            with open("members.csv", 'w', newline='', encoding="utf-8") as file:
                writer = csv.DictWriter(file, field_name)
                writer.writeheader()
                writer.writerows(updated_list)
            return f"Deletion succesful!!\n"

    def total_members(self):
        members = 0
        with open("members.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                members += 1
        return f"Total Members = {members}\n"