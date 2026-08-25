from services.product_manager import ProductManager
from services.supplier_manager import SupplierManager
from services.inventory_manager import InventoryManager
from enum import Enum



class OPTION(Enum):
    PRODUCT_MANAGEMENT = 1
    SUPPLIER_MANAGEMENT = 2
    STOCK_MANAGEMENT = 3
    REPORTS = 4

class PRODUCT_OPERATIONS(Enum):
    ADD_PRODUCT = 1
    VIEW_PRODUCTS = 2
    SEARCH_PRODUCT = 3
    UPDATE_PRODUCT = 4
    DELETE_PRODUCT = 5

class SUPPLIER_OPERATIONS(Enum):
    ADD_SUPPLIER = 1
    VIEW_SUPPLIERS = 2
    SEARCH_SUPPLIER = 3
    UPDATE_SUPPLIER = 4
    DELETE_SUPPLIER = 5

class TRANSACTION_OPERATIONS(Enum):
    STOCK_IN = 1
    STOCK_OUT = 2
    STOCK_ADJUSTMENT = 3

class REPORTS(Enum):
    INVENTORY_REPORT = 1
    CHECK_LOW_STOCK_PRODUCT = 2
    VIEW_TRANSACTION_RECORD = 3
    INVENTORY_VALUE = 4
    INVENTORY_SUMMARY = 5

product_manager = ProductManager()
supplier_manager = SupplierManager()
inventory_manager = InventoryManager()

def reports():

    def select_option():
        while True:
            try:
                print("*************************************")
                print("\t\tReports")
                print("*************************************\n")
                print("1. Inventory Report")
                print("2. Check low-stock Products")
                print("3. View Transaction Records")
                print("4. Inventory Value")
                print("5. Inventory Summary")
                print("6. Exit\n")
                option = int(input("Select an option: "))

                if option in range(1, 7):
                    return option
                raise ValueError
            except ValueError:
                print("Input must be in [1, 6]!!\n")
    
    operations = {
        REPORTS.INVENTORY_REPORT: product_manager.inventory_report,
        REPORTS.CHECK_LOW_STOCK_PRODUCT: product_manager.check_low_stock,
        REPORTS.INVENTORY_VALUE: product_manager.inventory_value,
        REPORTS.VIEW_TRANSACTION_RECORD: inventory_manager.view_transactions,
        REPORTS.INVENTORY_SUMMARY: product_manager.inventory_summary

    }

    option = select_option()
    while option != 6:
        print(operations[REPORTS(option)]())
        option = select_option()

def stock_management():

    def select_option():
        while True:
            try:
                print("*************************************")
                print("\tTransaction Management")
                print("*************************************\n")
                print("1. Stock In")
                print("2. Stock Out")
                print("3. Stock Adjustment")
                print("4. Exit\n")
                option = int(input("Select an option: "))

                if option in range(1,5):
                    return option
                raise ValueError
            except ValueError:
                print("Input must be in [1,4]!!\n")
    

    operations = {
        TRANSACTION_OPERATIONS.STOCK_IN: inventory_manager.stock_in,
        TRANSACTION_OPERATIONS.STOCK_OUT: inventory_manager.stock_out,
        TRANSACTION_OPERATIONS.STOCK_ADJUSTMENT: inventory_manager.stock_adjustment
    }

    option = select_option()
    while (option != 4):
        print(operations[TRANSACTION_OPERATIONS(option)]())
        option = select_option()



def supplier_management():

    def select_option():
        while True:
            try:
                print("*************************************")
                print("\tSupplier Management")
                print("*************************************\n")
                print("1. Add supplier")
                print("2. View all suppliers")
                print("3. Search supplier")
                print("4. Update supplier")
                print("5. Delete supplier")
                print("6. Exit\n")
                option = int(input("Select an option: "))
                if option in range(1,7):
                    return option
                raise ValueError
            except ValueError:
                print("Invalid Input.Value must be in range [1,5]!!\n")
    
    operations = {
        SUPPLIER_OPERATIONS.ADD_SUPPLIER: supplier_manager.add_supplier,
        SUPPLIER_OPERATIONS.VIEW_SUPPLIERS: supplier_manager.view_suppliers,
        SUPPLIER_OPERATIONS.SEARCH_SUPPLIER: supplier_manager.search_supplier,
        SUPPLIER_OPERATIONS.UPDATE_SUPPLIER: supplier_manager.update_supplier,
        SUPPLIER_OPERATIONS.DELETE_SUPPLIER: supplier_manager.delete_supplier
}
    option = select_option()

    while option != 6:
        print(operations[SUPPLIER_OPERATIONS(option)]())
        option = select_option()


def product_management():

    def select_option():
        while True:
            try:
                print("*************************************")
                print("\tProduct Management")
                print("*************************************\n")
                print("1. Add product")
                print("2. View all products")
                print("3. Search product")
                print("4. Update product")
                print("5. Delete product")
                print("6. Exit\n")
                option = int(input("Select an option: "))
                if option in range(1,7):
                    return option
                raise ValueError
            except ValueError:
                print("Invalid Input.Value must be in range [1,6]!!\n")
    
    operations = {
        PRODUCT_OPERATIONS.ADD_PRODUCT: product_manager.add_product,
        PRODUCT_OPERATIONS.VIEW_PRODUCTS: product_manager.view_products,
        PRODUCT_OPERATIONS.SEARCH_PRODUCT: product_manager.search_product,
        PRODUCT_OPERATIONS.UPDATE_PRODUCT: product_manager.update_product,
        PRODUCT_OPERATIONS.DELETE_PRODUCT: product_manager.delete_product
    }
    while True:
        option = select_option()
        if option == 6:
            break
        result = operations[PRODUCT_OPERATIONS(option)]()
        print(result)

def start():

    def select_option():
        while True:
            try:
                print("===============================================")
                print("\tINVENTORY MANAGEMENT SYSTEM]")
                print("===============================================")
                print("1. Product Management")
                print("2. Supplier Management")
                print("3. Stock Management")
                print("4. Reports")
                print("5. Exit")
                option = int(input("Select an option: "))
                if option in range(1,6):
                    return option
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input! Value should be in(1,5).\n")

    operations = {
        OPTION.PRODUCT_MANAGEMENT: product_management,
        OPTION.SUPPLIER_MANAGEMENT: supplier_management,
        OPTION.STOCK_MANAGEMENT: stock_management,
        OPTION.REPORTS: reports

    }

    option = select_option()
    while option != 5:
        operations[OPTION(option)]()
        option = select_option()

start()
