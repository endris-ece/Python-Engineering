from models.customer import Customer
from models.account import Account
from utilities.random_generator import RandomGenerator
from services.customer_manager import CustomerManager
import csv

class AccountManager:

    def __init__(self):
        self.random_generator = RandomGenerator()
        self.customer_manager = CustomerManager()

    def create_account(self):
        customer = self.customer_manager.create_customer()
        acount_number = self.random_generator.generate_account_number()
        account_type = input("Enter account type: (Savings or Business):\n:")
        while True:
            try:
                balance = float(input("Enter initial balance: "))
                break
            except ValueError:
                print("Balance must be a number.")

        account = Account(acount_number, customer, balance, account_type)

        account_row = [account.account_number, account.customer.c_ID, account.customer.f_name, account.customer.s_name, account.customer.phone, account.customer.email, account.customer.address, account.balance, account.account_type]
        with open("accounts.csv", 'a', newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(account_row)

        return f"{account} \nCreated succesfully!!"

    def view_accounts(self):

        output = ""
        with open("accounts.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                output = f"{output}\n{row["account_number"]}   |   {row["customer_Id"]}   |   {row["first_name"]}   |   {row["second_name"]}   |   {row["phone_number"]}   |   {row["email"]}   |   {row["address"]}   |   {row["balance"]}   |   {row["account_type"]}\n"

            return output

    def enter_account(self):
        while True:
            try:
                account_number = input("Enter the account number: ")
                if account_number.isdigit():
                    return account_number
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Account Number!!\n")
            except Exception as e:
                print(e)

    def search_account(self):
        acc_number = self.enter_account()

        with open("accounts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["account_number"] == acc_number:
                    return f"Found!\n{row}"
            
            return f"Account Not Found!!"

    def close_account(self):
        acc_number = self.enter_account()
        ramaining_row = []
        with open("accounts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["account_number"] != acc_number:
                    ramaining_row.append(row)
            
                
        with open("accounts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(ramaining_row)

        return f"Account {acc_number} deleted successfully!"


    