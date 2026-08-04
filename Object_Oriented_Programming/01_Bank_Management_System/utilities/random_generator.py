import random
import csv


class RandomGenerator:

    def generate_ID(self):

        while(True):
            exist = False
            rand = random.randint(1000, 9999)
            Id = f"CustId{rand}"
            with open("customers.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["customer_Id"] == Id:
                        exist = True
                if not exist:
                    return Id
    
    def  generate_account_number(self):

        while(True):
            exist = False
            rand = random.randint(10000000, 99999999)
            account_number = f"10000{rand}"
            with open("accounts.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["account_number"] == account_number:
                        exist = True
                if not exist:
                    return account_number
    