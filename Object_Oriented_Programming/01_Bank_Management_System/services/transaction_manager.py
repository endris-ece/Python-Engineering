import csv

class Transactions:

    def enter_account(self):
        while True:
            try:
                account_number = input("Enter the account number: ")
                with open("accounts.csv", 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row["account_number"] == account_number:
                            return account_number
                raise ValueError
            except ValueError:
                print("Invalid Account Number!!\n")
            except Exception as e:
                print(e)

    def enter_amount(self):
        while True:
            try:
                money = int(input("Enter amount: "))
                if money > 0:
                    return money
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Amount!!\n")
            except Exception as e:
                print(e)

    def deposit(self):

        amount = self.enter_amount()
        acc_number = self.enter_account()
        rows = []
        with open("accounts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames

            for row in reader:
                if row["account_number"] == acc_number:
                    row["balance"] = f"{int(row["balance"]) + amount}"
                rows.append(row)
        with open("accounts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames= field_names)
            writer.writeheader()
            writer.writerows(rows)

        with open("accounts.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["account_number"] == acc_number:
                    return f"operation successful!!\n{row}"
            return f"Account Not Found!!\n"

    def transfer(self):

        updated = []
        def enter_transfer_account():
            print("Account Transfer From")
            return self.enter_account()
        def enter_reciever_account():
            print("Reciever Account")
            return self.enter_account()

        def enter_transfer_amount(account):
            while True:
                try:
                    transfer_amount = self.enter_amount()
                    
                    with open("accounts.csv", 'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row["account_number"] == account:
                                if transfer_amount > int(row["balance"]):
                                    raise ValueError

                    return transfer_amount
                except ValueError:
                    print(f"Account does not have enough amount.\n")
                except Exception as e:
                    print(e)

        transfer_acc = enter_transfer_account()
        reciever_acc = enter_reciever_account()
        amount = enter_transfer_amount(transfer_acc)

        with open("accounts.csv", 'r') as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["account_number"] == transfer_acc:
                    row["balance"] = f"{int(row["balance"]) - amount}"
                elif row["account_number"] == reciever_acc:
                    row["balance"] = f"{int(row["balance"]) + amount}"
                updated.append(row)

        with open("accounts.csv", 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = field_names)
            writer.writeheader()
            writer.writerows(updated)

        return f"Transfer Successfull!!\n"


    def withdraw(self):
        acc_number = self.enter_account()
        def enter_withdrawal_amount():
            while True:
                try:
                    amount = self.enter_amount()
                    with open("accounts.csv", 'r') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if row["account_number"] == acc_number:
                                if int(row["balance"]) < amount:
                                    raise ValueError
                    return amount

                except ValueError:
                    print(f"Can't withdraw {amount} amount of money")
                except Exception as e:
                    print(e)
        amount = enter_withdrawal_amount()
        updated = []
        with open("accounts.csv", 'r') as file:
            reader = csv.DictReader(file)
            field_names = reader.fieldnames
            for row in reader:
                if row["account_number"] == acc_number:
                    row["balance"] = f"{int(row["balance"]) - amount}"
                updated.append(row)        

        with open("accounts.csv", 'w', newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames= field_names)
            writer.writeheader()
            writer.writerows(updated)
        return f"Withdrawal successful!!"