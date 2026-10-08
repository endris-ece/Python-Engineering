import numpy as np
from enum import Enum
from matrix_operations import *

class MainMenu(Enum):
    MATRIX_PROPERTIES = 1
    BASIC_MATRIX_INFORMATION = 2
    MATRIX_OPERATIONS = 3
    SOLVE_LINEAR_SYSTEM_EQUATIONS = 4
    EXIT = 5

class MatrixProperties(Enum):
    SHAPE = 1
    NUMBER_OF_DIMENSIONS = 2
    NUMBER_OF_ELEMENTS = 3
    DATA_TYPE = 4
    EXIT = 5

class BasicInformation(Enum):
    DETERMINANT = 1
    INVERSE = 2
    RANK = 3
    EIGEN_VALUES = 4
    EIGEN_VECTORS = 5
    TRANSPOSE = 6
    EXIT = 7

class MatrixOperation(Enum):
    ADDITION = 1
    SUBTRACTION = 2
    SCALAR_MULTIPLICATION = 3
    MATRIX_MULTIPLICATION = 4
    EXIT = 5

def generate_menu(menu):
    while True:
        try:

            for operation in menu:
                print(f"{operation.value}. {operation.name}")
            option = int(input("Select an option: "))
            if option in range(1, len(menu) + 1):
                return menu(option)
            raise ValueError
        except ValueError:
            print(f"Input must be in [1,{len(menu)}]!!\n")

def generate_matrix(rows, columns):


    entries = []
    for r in range(rows):
        row = []
        for c in range(columns):
            entry = float(input(f"Enter value for row {r+1} and column {c+1} : "))
            row.append(entry)
        entries.append(row)
    return np.array(entries)
     
def matrix_properties():

    operations = {
        MatrixProperties.SHAPE: find_shape,
        MatrixProperties.NUMBER_OF_DIMENSIONS: find_number_of_dimensions,
        MatrixProperties.NUMBER_OF_ELEMENTS: find_number_of_elements,
        MatrixProperties.DATA_TYPE: find_data_type
    }

    option = generate_menu(MatrixProperties)

    while option != MatrixProperties.EXIT:
        try:
            row = int(input("Enter the number of row: "))
            column = int(input("Enter the number of column: "))
            
            if row > 0 and row <= 10 and column > 0 and column <= 10:
                matrix = generate_matrix(row, column)
                print(operations[option](matrix))

            if row > 10 or column > 10:
                raise ValueError("Matrix row/column must be in range [1, 10]!!\n")

            option = generate_menu(MatrixProperties)
        except ValueError as e:
            print(e)


def basic_information():

    operations = {
        BasicInformation.DETERMINANT: find_determinant,
        BasicInformation.INVERSE: find_inverse,
        BasicInformation.RANK: find_rank,
        BasicInformation.EIGEN_VALUES: find_eigen_values,
        BasicInformation.EIGEN_VECTORS: find_eigen_vectors,
        BasicInformation.TRANSPOSE: find_transpose
    }
    option = generate_menu(BasicInformation)

    while option != BasicInformation.EXIT:
        try:

            if option == BasicInformation.TRANSPOSE:
                row = int(input("Enter the number of row: "))
                column = int(input("Enter the number of column: "))
            else:
                row = int(input("Enter the number of row/column of square matrix: "))
                column = row
            
            if 1 <= row <= 10 and 1 <= column <= 10:
                matrix = generate_matrix(row, column)
                print(operations[option](matrix))

            else:
                raise ValueError("Matrix row/column must be in range [1, 10]!!\n")

            option = generate_menu(BasicInformation)
        except ValueError as e:
            print(e)



def matrix_operation():
    operations = {
        MatrixOperation.ADDITION: addition,
        MatrixOperation.SUBTRACTION: subtraction,
        MatrixOperation.SCALAR_MULTIPLICATION: scalar_multiplication,
        MatrixOperation.MATRIX_MULTIPLICATION: matrix_multiplication,

    }

    option = generate_menu(MatrixOperation)
    while option != MatrixOperation.EXIT:
        try:
            if option in [MatrixOperation.ADDITION, MatrixOperation.SUBTRACTION]:
                row = int(input("Enter the number of row of the matrices: "))
                column = int(input("Enter the number of column of the matrices: "))

                if not (1 <= row <= 10 and 1 <= column <= 10):                    
                    raise ValueError("Number of rows/columns must be in range [1, 10]!!")

                print("Enter entries for First Matrix\n")
                matrix1 = generate_matrix(row, column)
                print("")
                print("Enter entries for Second Matrix\n")
                matrix2 = generate_matrix(row, column)

            elif option == MatrixOperation.SCALAR_MULTIPLICATION:
                matrix1 = float(input("Enter the scalar multiplier: "))

                row = int(input("Enter the number of row of the matrix: "))
                column = int(input("Enter the number of the column of the matrix: "))

                if not (1 <= row <= 10 and 1 <= column <= 10):                    
                    raise ValueError("Number of rows/columns must be in range [1, 10]!!")

                matrix2 = generate_matrix(row, column)

            elif option == MatrixOperation.MATRIX_MULTIPLICATION:
                
                row1 = int(input("Enter the number of row of the first matrix: "))
                column1 = int(input("Enter the number of the column of the first matrix/row of the second matrix: "))
                row2 = column1
                column2 = int(input("Enter the number of column of the second matrix: "))

                if not (1 <= row1 <= 10 and 1 <= column1 <= 10 and 1 <= row2 <= 10 and 1 <= column2 <= 10):
                    raise ValueError("Number of rows/columns must be in range [1, 10]!!")

                print("Enter entries for First Matrix\n")
                matrix1 = generate_matrix(row1, column1)
                print("")
                print("Enter entries for Second Matrix\n")
                matrix2 = generate_matrix(row2, column2)

            print(operations[option](matrix1, matrix2))
            option = generate_menu(MatrixOperation)

        except ValueError as e:
            print(e)

def solve_linear_systems():
    
    while True:
        try:
            B = []

            num = int(input("Enter the number of linear equation: "))
            if not (num in range(11)):
                raise ValueError("Input must be in range [1, 10]!!\n")

            matrix = generate_matrix(num, num)
            print("")
            for n in range(num):
                entry = float(input(f"Enter column vector of equation{n+1}: "))
                B.append(entry)
            b = np.array(B)
            return np.linalg.solve(matrix, b)
        except ValueError as e:
            print(e)



def start():
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("\tMATRIX ANALYSIS")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

    operations = {
        MainMenu.MATRIX_PROPERTIES: matrix_properties,
        MainMenu.BASIC_MATRIX_INFORMATION: basic_information,
        MainMenu.MATRIX_OPERATIONS: matrix_operation,
        MainMenu.SOLVE_LINEAR_SYSTEM_EQUATIONS: solve_linear_systems
    }

    option = generate_menu(MainMenu)
    while option != MainMenu.EXIT:
        print(operations[option]())
        option = generate_menu(MainMenu)


start()