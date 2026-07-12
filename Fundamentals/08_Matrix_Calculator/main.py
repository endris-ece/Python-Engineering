operations = ["Matrix Addition", "Matrix Subtraction", "Scalar Multiplication", "Matrix Multiplication", "Transpose", "Determinant_2x2", "Inverse_2x2"]


#Operation selection
def select_operation():
    while True:
        try:
            operation = int(input(f"Choose the operation you want to perform:\n{'\n'.join(f'{i+1}. {operate}' for i, operate in enumerate(operations))}\n: "))
            if operation in range(1,len(operations) + 1):
                return operations[operation - 1]
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid Input, Input should be in {[1, len(operations)]}")
        except Exception as e:
            print(e)


#Row and Column number handling
def single_matrix_row_column():
    matrix_row_column = []
    while True:
        try:
            row_number = int(input(f"Enter the number of row:\n"))
            column_number = int(input(f"Enter the number of column:\n"))
            if 0 < row_number <= 10 and 0 < column_number <= 10:
                matrix_row_column.append(row_number)
                matrix_row_column.append(column_number)
            else:
                raise ValueError
            return matrix_row_column
        except ValueError:
            print("Invalid Input: number of row/column must be in (1,10):\n************************************************************")
        except Exception as e:
            print(e)

def double_matrix_row_column():
    matrix = {"matrix_A": [],
    "matrix_B": []}
    while True:
        try:
            for key in matrix.keys():
                row_number = int(input(f"Enter the number of ROW for {key}:\n"))
                column_number = int(input(f"Enter the number of COLUMN for {key}:\n"))
                if 0 < row_number <= 10 and 0 < column_number <= 10:
                    matrix[key].append(row_number)
                    matrix[key].append(column_number)
                else:
                    raise ValueError
            return matrix
        except ValueError:
            print("Invalid Input: number of row/column must be in (1,10):\n************************************************************")
        except Exception as e:
            print(e)


#Input values handling
def enter_addition_inputs():
    def addition_row_column():
        while True:
            row_column_number = double_matrix_row_column()
            if row_column_number["matrix_A"] == row_column_number["matrix_B"]:
                return row_column_number
            else:
                print("Number of row and column of the 2 matrix must be the same!\n************************************************************")
    row_column_number = addition_row_column()
    matrix_A = []
    matrix_B = []
    while True:
        try:
            for key in row_column_number.keys():
                for i in range(row_column_number[key][0]):
                    number_list = []
                    for j in range(row_column_number[key][1]):
                        input_value = float(input(f"Enter the value of: \n{key} entry({i+1},{j+1})\n:"))
                        if -1000 <= input_value <= 1000:
                            number_list.append(input_value)
                        else:
                            raise ValueError
                    if key == "matrix_A":
                        matrix_A.append(number_list)
                    else:
                        matrix_B.append(number_list)
            return {"matrix_A": matrix_A, "matrix_B": matrix_B, "row_column_number": row_column_number["matrix_A"]}
        except ValueError:
            print("Invalid Input, entry value should be in [-1000, 1000]:\n************************************************************")
        except Exception as e:
            print(e)

def enter_subtraction_inputs():
    return enter_addition_inputs()

def enter_matrix_multiplication_inputs():
    def multiplication_row_column():
        while True:
            row_column_number = double_matrix_row_column()
            if row_column_number["matrix_A"][1] == row_column_number["matrix_B"][0]:
                return row_column_number
            else:
                print("column of matrix A must equal row of matrix B:\n************************************************************")

    row_column_number = multiplication_row_column()
    matrix_A = []
    matrix_B = []
    while True:
        try:
            for key in row_column_number.keys():
                for i in range(row_column_number[key][0]):
                    number_list = []
                    for j in range(row_column_number[key][1]):
                        input_value = float(input(f"Enter the value of: \n{key} entry({i+1},{j+1})\n: "))
                        if -1000 <= input_value <= 1000:
                            number_list.append(input_value)
                        else:
                            raise ValueError
                    if key == "matrix_A":
                        matrix_A.append(number_list)
                    else:
                        matrix_B.append(number_list)
            return {"matrix_A": matrix_A, "matrix_B": matrix_B, "row_column_number": row_column_number}
        except ValueError:
            print("Invalid Input, entry must be in [-1000, 1000]:\n************************************************************")
        except Exception as e:
            print(e)


def enter_scalar_multiplication_inputs():
    row_column_number = single_matrix_row_column()
    matrix = []
    while True:
        try:
            sc = float(input("Enter the value of the scalar multiplier\n: "))
            if -1000 <= sc <= 1000:
                scalar = sc
            else:
                raise ValueError
            for i in range(row_column_number[0]):
                number_list = []
                for j in range(row_column_number[1]):
                    input_value = float(input(f"Enter the value of:\n entry({i+1},{j+1})\n:"))
                    if -1000 <= input_value <= 1000:
                        number_list.append(input_value)
                    else:
                        raise ValueError
                matrix.append(number_list)
            return {"multiplier": scalar, "matrix": matrix, "row_column_number":row_column_number}
        except ValueError:
            print("Invalid Input, entry must be in [-1000, 1000]:\n************************************************************")
        except Exception as e:
            print(e)


def enter_transpose_inputs():
    row_column_number = single_matrix_row_column()
    matrix = []
    while True:
        try:
            for i in range(row_column_number[0]):
                number_list = []
                for j in range(row_column_number[1]):
                    input_value = float(input(f"Enter the value of:\n entry({i+1},{j+1})\n:"))
                    if -1000 <= input_value <= 1000:
                        number_list.append(input_value)
                    else:
                        raise ValueError
                matrix.append(number_list)
            return {"matrix": matrix, "row_column_number": row_column_number}
        except ValueError:
            print("Invalid Input, entry must be in [-1000, 1000]:\n************************************************************")
        except Exception as e:
            print(e)


def enter_determinant_2x2_inputs():
    matrix = []
    while True:
        try:
            for i in range(2):
                number_list = []
                for j in range(2):
                    input_value = float(input(f"Enter the value of\n entry({i+1},{j+1})\n:"))
                    if input_value < 1000:
                        number_list.append(input_value)
                    else:
                        raise ValueError
                matrix.append(number_list)
            return matrix
        except ValueError:
            print("Invalid Input")
        except Exception as e:
            print(e)    

def enter_inverse_2x2_inputs():
    return enter_determinant_2x2_inputs()

#Calculations
def calculate_matrix_addition():
    input_values = enter_addition_inputs()
    row_column_number = input_values["row_column_number"]
    matrix_resut = []
    for row in range(row_column_number[0]):
        row_sum = []
        for column in range(row_column_number[1]):
            entry_sum = input_values["matrix_A"][row][column] + input_values["matrix_B"][row][column]
            row_sum.append(entry_sum)
        matrix_resut.append(row_sum)
    return {"Input A": input_values["matrix_A"],"Input B": input_values["matrix_B"],"Result":matrix_resut}

def calculate_matrix_subtraction():
    input_values = enter_subtraction_inputs()
    row_column_number = input_values["row_column_number"]
    matrix_resut = []
    for row in range(row_column_number[0]):
        row_result = []
        for column in range(row_column_number[1]):
            entry = input_values["matrix_A"][row][column] - input_values["matrix_B"][row][column]
            row_result.append(entry)
        matrix_resut.append(row_result)
    return {"Input A": input_values["matrix_A"],"Input B": input_values["matrix_B"],"Result":matrix_resut}

def calculate_matrix_multiplication():
    input_values = enter_matrix_multiplication_inputs()
    row_column_number = input_values["row_column_number"]
    matrix_resut = []
    for row_A in range(row_column_number["matrix_A"][0]):
        row_result = []
        for column_B in range(row_column_number["matrix_B"][1]):
            result_entry_sum = 0
            for column in range(row_column_number["matrix_A"][1]):
                entry_product = input_values["matrix_A"][row_A][column] * input_values["matrix_B"][column][column_B]
                result_entry_sum += entry_product
            
            row_result.append(result_entry_sum)
        matrix_resut.append(row_result)
    return {"Input A": input_values["matrix_A"],"Input B": input_values["matrix_B"],"Result":matrix_resut}

def calculate_scalar_matrix_multiplication():
    input_values = enter_scalar_multiplication_inputs()
    row_column_number = input_values["row_column_number"]
    scalar = [[input_values["multiplier"]]]
    matrix_result = []
    for row in range(row_column_number[0]):
        row_result = []
        for column in range(row_column_number[1]):
            entry_product = input_values["matrix"][row][column] * scalar[0][0]
            row_result.append(entry_product)
        matrix_result.append(row_result)
    return {"Input A": scalar,"Input B": input_values["matrix"],"Result":matrix_result}


def calculate_2x2_matrix_determinant():
    input_values = enter_determinant_2x2_inputs()
    matrix_result = [[input_values[0][0]*input_values[1][1]] - input_values[0][1]*input_values[1][0]]
    return {"Input": input_values, "Result": matrix_result}


def calculate_matrix_transpose():
    input_values = enter_transpose_inputs()
    row_column_number = input_values["row_column_number"]
    matrix_result = []
    for row in range(row_column_number[1]):
        row_result = []
        for column in range(row_column_number[0]):
            entry = input_values["matrix"][column][row]
            row_result.append(entry)
        matrix_result.append(row_result)
    return {"Input": input_values["matrix"], "Result": matrix_result}


def calculate_2x2_matrix_inverse():
    while True:
        input_values = enter_determinant_2x2_inputs()
        determinant = input_values[0][1]*input_values[1][0] - input_values[0][0]*input_values[1][1]
        if determinant != 0:
            break
        else:
            print("You entered is a Singular matrix\n************************************************************")

    matrix_result = []
    for row in range(2):
        row_result = []
        for column in range(2):
            if row != column:
                entry = -input_values[row][column]
            elif row == 0:
                entry = input_values[1][1]
            else:
                entry = input_values[0][0]
            row_result.append(entry/determinant)
        matrix_result.append(row_result)
    return {"Input": input_values, "Result":matrix_result}


#Operation calling
calculations = {"Matrix Addition": calculate_matrix_addition,
"Matrix Subtraction": calculate_matrix_subtraction,
"Scalar Multiplication": calculate_scalar_matrix_multiplication,
"Matrix Multiplication": calculate_matrix_multiplication,
"Transpose": calculate_matrix_transpose,
"Determinant_2x2": calculate_2x2_matrix_determinant,
"Inverse_2x2": calculate_2x2_matrix_inverse}

def display():
    output = ""
    calculate = select_operation()
    calculation = calculations[calculate]()
    for key, value in calculation.items():
        number_list = ""
        for row in range(len(value)):
            for column in range(len(value[row])):
                number_list = f"{number_list}\t{calculation[key][row][column]}"
            number_list = f"{number_list}\n"
        output = f"{output}\n{key} = \n{number_list}"

    return output


print(display())