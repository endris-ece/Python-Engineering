gates = ["NOT", "OR", "AND", "NOR", "NAND", "XOR", "XNOR"]

def select_gate():
    while True:
        try:
            gate_number = int(input(F"Choose the gate:\n{'\n'.join(f'{i + 1}. {gate}' for i, gate in enumerate(gates))}\n: "))
            if gate_number - 1 in range(len(gates)):
                return gates[gate_number - 1]
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid Input. input should be in range(1, {len(gates)}")
        except Exception as e:
            print(e)


def enter_not_input():
    while True:
        try:
            input_value = int(input("Enter the input A = "))
            if input_value in [0, 1]:
                return input_value
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid input. input should be 0 or 1")
        except Exception as e:
            print(e)


def enter_inputs():
    def enter_input_number():
        while True:
            try:
                input_number = int(input("Enter the number of inputs\n: "))
                if 2 <= input_number <= 26:
                    return input_number
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input. Value should be between 2 and 26")
            except Exception as e:
                print(e)
    number_of_input = enter_input_number()    
    input_values = []
    while True:
        try:
            for i in range(number_of_input):
                input_value = int(input(f"Enter input {i + 1} = "))
                if input_value in [0, 1]:
                    input_values.append(input_value)
                else:
                    raise ValueError
            return input_values
        except ValueError:
            print("Invalid Input. Value should be 0 or 1")
        except Exception as e:
            print(e)

def calculate_not_gate(input_value):
    if input_value[0] == 0:
        return 1
    else:
        return 0

def calculate_or_gate(inputs):
    if 1 in inputs:
        return 1
    else:
        return 0

def calculate_and_gate(inputs):
    if 0 in inputs:
        return 0
    else:
        return 1

def calculate_nor_gate(inputs):
    if 1 in inputs:
        return 0
    else:
        return 1

def calculate_nand_gate(inputs):
    if 0 in inputs:
        return 1
    else:
        return 0

def calculate_xor_gate(inputs):
    ones = sum(inputs)

    if ones % 2 == 1:
        return 1
    else:
        return 0

def calculate_xnor_gate(inputs):
    ones = sum(inputs)
    if ones % 2 == 0:
        return 1
    else:
        return 0

calculations = {"NOT": calculate_not_gate,
"OR": calculate_or_gate,
"AND": calculate_and_gate,
"NOR": calculate_nor_gate,
"NAND": calculate_nand_gate,
"XOR": calculate_xor_gate,
"XNOR": calculate_xnor_gate}

def output_display():
    gate = select_gate()

    if gate == "NOT":
        input_values = [enter_not_input()]
    else:
        input_values = enter_inputs()

    print(f"==================\nGATE: {gate}\n::\nInputs:\n{'\n'.join(f'{chr(65 + i)} = {value}' for i, value in enumerate(input_values))}\n::\nOUTPUT:\n{calculations[gate](input_values)}\n==================")

output_display()