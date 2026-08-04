from services.account_manager import AccountManager
from services.customer_manager import CustomerManager
from services.transaction_manager import Transactions
from enum import Enum
import csv

account_manager = AccountManager()
customer_manager = CustomerManager()
transaction_manager = Transactions()

def customer_management():

    class services(Enum):
        CREATE_CUSTOMER = 1
        VIEW_CUSTOMERS = 2
        SEARCH_CUSTOMER = 3
        UPDATE_CUSTOMER = 4
        DELETE_CUSTOMER = 5

    def customer_service():

        while True:
            try:

                print("====================================================")
                print("Customer Management")
                print("====================================================\n")
                print("1. Add Customer")
                print("2. View All Customers")
                print("3. Search Cutomers")
                print("4. Update Customer")
                print("5. Delete Customer")
                print("6. Exit\n")
                
                option = int(input("Select an option: "))

                if option in range(1,7):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input, value should be in (1,6)\n")
            except Exception as e:
                print(e)

    operations ={
        services.CREATE_CUSTOMER: customer_manager.create_customer,
        services.VIEW_CUSTOMERS: customer_manager.view_customers,
        services.SEARCH_CUSTOMER: customer_manager.search_customer,
        services.UPDATE_CUSTOMER: customer_manager.update_customer,
        services.DELETE_CUSTOMER: customer_manager.delete_customer
    }
    service = customer_service()
    while service != 6:
        print(operations[services(service)]())
        service = customer_service()


def account_management():

    class services(Enum):
        CREATE_ACCOUNT = 1
        VIEW_ACCOUNTS = 2
        SEARCH_ACCOUNT = 3
        CLOSE_ACCOUNT = 4

    def account_service():

        while True:
            try:

                print("====================================================")
                print("Account Management")
                print("====================================================\n")
                print("1. Create Account")
                print("2. View All Accounts")
                print("3. Search Account")
                print("4. Delete Account")
                print("5. Exit\n")
                
                option = int(input("Select an option: "))

                if option in range(1,6):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input, value should be in (1,5)\n")
            except Exception as e:
                print(e)

    operations ={
        services.CREATE_ACCOUNT: account_manager.create_account,
        services.SEARCH_ACCOUNT: account_manager.search_account,
        services.VIEW_ACCOUNTS: account_manager.view_accounts,
        services.CLOSE_ACCOUNT: account_manager.close_account
    }
    service = account_service()
    while service != 5:
        print(operations[services(service)]())
        service = account_service()


def transactions():

    class services(Enum):
        DEPOSIT = 1
        WITHDRAW = 2
        TRANSFER = 3
    def operation():
        while True:
            try:
                print("====================================================")
                print("Transactions")
                print("====================================================\n")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. Exit")

                option = int(input("select an option: "))

                if option in range(1,5):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input, Value should be in (1,4)\n")
            except Exception as e:
                print(e)
    operations ={
        services.DEPOSIT: transaction_manager.deposit,
        services.TRANSFER: transaction_manager.transfer,
        services.WITHDRAW: transaction_manager.withdraw,

    }
    option = operation()
    while option != 4:
        print(operations[services(option)]())
        option = operation()


def reports():
    customers_info = ""
    accounts_info = ""
    customer_amount = 0
    total_balance = 0
    try:
        with open("customers.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customer_amount += 1
                customers_info = f"{customers_info}\n{row}"
        with open("accounts.csv", 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                accounts_info = f"{accounts_info}\n{row}"
                total_balance = total_balance + int(row["balance"])
    except FileNotFoundError:
        print("File not found")
    print(f"Customers Information\nAmount of customers = {customer_amount}\n\n{customers_info}\n\nAccounts Information\nTotal Balance = {total_balance}\n\n{accounts_info}")

def start():

    class options(Enum):
        CUSTOMER_MANAGEMENT = 1
        ACCOUNT_MANAGEMENT = 2
        TRANSACTION_MANAGEMENT = 3
        REPORTS = 4
    
    def select_option():

        while True:
            try:
                print("====================================================")
                print("BANK MANAGEMENT")
                print("====================================================\n")
                print("1. Customer Management")
                print("2. Account Management")
                print("3. Transactions")
                print("4. Reports")
                print("5. Exit\n")

                option = int(input("Select an option: "))

                if option in range(1,6):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input, value should be in (1,5)\n")
            except Exception as e:
                print(e)
    operations ={
        options.ACCOUNT_MANAGEMENT: account_management,
        options.CUSTOMER_MANAGEMENT: customer_management,
        options.TRANSACTION_MANAGEMENT: transactions,
        options.REPORTS: reports    
    }
    option = select_option()
    while option != 5:
        operations[options(option)]()
        option = select_option()


start()