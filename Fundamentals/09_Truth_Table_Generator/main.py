
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

def input_numbers(gate):
    if gate == "NOT":
        return 1
    else:
        while True:
            try:
                input_number = int(input("Enter the number of inputs\n: "))
                if 10 >= input_number >= 2:
                    return input_number
                else:
                    raise ValueError
            except ValueError:
                print("Input number should be between 2 and 10:\n************************************************************")
            except Exception as e:
                print(e)

def input_generator(gate):
    input_number = input_numbers(gate)
    inputs = []

    for i in range(2 ** input_number):
        number = i
        row = []

        for _ in range(input_number):
            row.insert(0, number % 2)
            number //= 2

        inputs.append(row)

    return inputs

def generate_NOT_gate():
    input_values = input_generator("NOT")
    result = []
    for row in input_values:
        result.append(1 - row[0])
    return {"Input": input_values, "Output": result}

def generate_OR_gate():
    input_values = input_generator("OR")
    result = []
    for input_value in input_values:
        if 1 in input_value:
            result.append(1)
        else:
            result.append(0)
    return {"Input": input_values, "Output": result}

def generate_AND_gate():
    input_values = input_generator("AND")
    result = []
    for input_value in input_values:
        if 0 in input_value:
            result.append(0)
        else:
            result.append(1)
    return {"Input": input_values, "Output": result}

def generate_NOR_gate():
    input_values = input_generator("NOR")
    result = []
    for input_value in input_values:
        if 1 in input_value:
            result.append(0)
        else:
            result.append(1)
    return {"Input": input_values, "Output": result}

def generate_NAND_gate():
    input_values = input_generator("NAND")
    result = []
    for input_value in input_values:
        if 0 in input_value:
            result.append(1)
        else:
            result.append(0)
    return {"Input": input_values, "Output": result}

def generate_XOR_gate():
    input_values = input_generator("XOR")
    result = []
    for input_value in input_values:
        ones = sum(input_value)
        if ones % 2 == 1:
            result.append(1)
        else:
            result.append(0)
    return {"Input": input_values, "Output": result}

def generate_XNOR_gate():
    input_values = input_generator("XNOR")
    result = []
    for input_value in input_values:
        ones = sum(input_value)
        if ones % 2 == 0:
            result.append(1)
        else:
            result.append(0)
    return {"Input": input_values, "Output": result}


generator = {"NOT": generate_NOT_gate,
"OR": generate_OR_gate,
"AND": generate_AND_gate,
"NOR": generate_NOR_gate,
"NAND": generate_NAND_gate,
"XOR": generate_XOR_gate,
"XNOR": generate_XNOR_gate}

def display():
    gate = select_gate()
    output = generator[gate]()
    table = ""
    inputs = ""
    bits = len(output["Input"][0])
    for i in range(len(output["Input"])):
        for j in range(len(output["Input"][i])):
            table = f"{table}\t{output["Input"][i][j]}"
        table = f"{table}\t| {output["Output"][i]}\n"
    for bit in range(bits):
        inputs = f"{inputs}\t{chr(65 + bit)}"

    return f"{inputs}\t| Output\n\n{table}"


print(display())