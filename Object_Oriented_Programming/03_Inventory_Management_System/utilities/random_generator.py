import random
import csv

class RandomGenerator:

    def generate_product_id(self):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            product_id = f"prod{rand}"
            with open("products.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["product_id"] == product_id:
                        exist = True
            if not exist:
                return product_id
                
    def generate_supplier_id(self):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            supplier_id = f"sup{rand}"
            with open("suppliers.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["supplier_id"] == supplier_id:
                        exist = True
            if not exist:
                return supplier_id

    def generate_transaction_id(self):
        while True:
            rand = random.randint(1000, 10000)
            exist = False
            transaction_id = f"transac{rand}"
            with open("transactions.csv", 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["transaction_id"] == transaction_id:
                        exist = True
            if not exist:
                return transaction_id