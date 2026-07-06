import math
quantities =[("power","Watt"), ("voltage", "Volt"), ("current", "Ampere"), ("resistance", "Ohm")]


def target_quantity():
    prompt = ""
    for i,quantity in enumerate(quantities):
        prompt = f"{prompt} {i+1}. {quantity[0]}\n"

    while True:
        try:
            target = int(input(f"Choose the quantity to calculate:\n{prompt}"))
            if target in range(1, len(quantities) + 1):
                return quantities[target -1]
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid Input, input should be in range {range(1,len(quantities))}")
        except Exception as e:
            print(e)


def enter_input(target):
    potential_available_inputs = [quantity[0] for quantity in quantities if quantity[0] != target[0]]

    def choose_available_inputs():
        prompt =""
        for i, quantity in enumerate(potential_available_inputs):
            if i == len(potential_available_inputs) - 1:
                prompt = f"{prompt} {i+1}. {quantity} and {potential_available_inputs[0]}\n"
            else:
                prompt = f"{prompt} {i+1}. {quantity} and {potential_available_inputs[i+1]}\n"
        available_inputs = []
        while True:
            try:
                available_input = int(input(f"Select the known quantities:\n{prompt}"))
                if available_input in range(1, len(potential_available_inputs) + 1):
                    if available_input == len(potential_available_inputs):
                        available_inputs.append(potential_available_inputs[available_input - 1])
                        available_inputs.append(potential_available_inputs[0])
                    else:
                        available_inputs.append(potential_available_inputs[available_input - 1])
                        available_inputs.append(potential_available_inputs[available_input])
                    return available_inputs
                else:
                    raise ValueError
                print(f"Invalid Input, input should be in range {1, len(potential_available_inputs)}")
            except ValueError:
                print(f"Invalid Input, input should an integer and be in range {1, len(potential_available_inputs)}")
            except Exception as e:
                print(e)
    
    selected_inputs = choose_available_inputs()
    while True:
        try:
            input_values = {}
            for quantity in selected_inputs:
                input_value = float(input(f"Enter the value of {quantity}:\n"))
                if input_value > 0:
                    input_values[quantity]= input_value
                elif input_value == 0:
                    print(f"{quantity} value can't be zero!")
                elif input_value < 0:
                    print(f"Please enter a positive number")
                else:
                    raise ValueError
            return input_values
        except ValueError:
            print(f"Invalid input")
        except Exception as e:
            print(e)


def calculate(input_quantities, tgt):
    target = tgt[0]
    input_quantity = [key for key in input_quantities.keys()]
    def calculate_power():
        if "power" in input_quantity:
            return input_quantities['power']
        elif "voltage" in input_quantity and "current" in input_quantity:
            return input_quantities['voltage'] * input_quantities['current']
        elif "voltage" in input_quantity and "resistance" in input_quantity:
            return (math.pow(input_quantities['voltage'], 2)) / input_quantities['resistance']
        elif "resistance" in input_quantity and "current" in input_quantity:
            return (math.pow(input_quantities['current'], 2)) * input_quantities['resistance']
    power = calculate_power()
    if target == 'power':
        output = power
    elif target == 'voltage':
        if 'current' in input_quantity:
            output = power / input_quantities['current']
        elif 'resistance' in input_quantity:
            output = math.sqrt(power * input_quantities['resistance'])
    elif target == 'current':
        if 'voltage' in input_quantity:
            output = power / input_quantities['voltage']
        elif 'resistance' in input_quantity:
            output = math.sqrt(power / input_quantities['resistance'])
    elif target == 'resistance':
        if 'voltage' in input_quantity:
            output = math.pow(input_quantities['voltage'], 2) / power
        elif 'current' in input_quantity:
            output = power / (math.pow(input_quantities['current'], 2))

    return f"{target} = {output:.3f} {tgt[1]}"



output_quantity = target_quantity()
print(calculate(enter_input(output_quantity), output_quantity))
