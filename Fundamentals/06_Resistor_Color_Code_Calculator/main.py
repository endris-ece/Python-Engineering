resistor_types = ["4 Bands", "5 Bands"]
digit_values = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Violet": 7,
    "Grey": 8,
    "White": 9}

multiplier_values = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10**4,
    "Green": 10**5,
    "Blue": 10**6,
    "Violet": 10**7,
    "Grey": 10**8,
    "White": 10**9,
    "Gold": 0.1,
    "Silver": 0.01,
    "Pink": 0.001}

tolerance_values = {
    "Brown": "± 1%",
    "Red": "± 2%",
    "Orange": "± 0.05%",
    "Yellow": "± 0.02%",
    "Green": "± 0.5%",
    "Blue": "± 0.25%",
    "Violet": "± 0.1%",
    "Grey": "± 0.01%",
    "Gold": "± 5%",
    "Silver": "± 10%"
    }

Four_Band_resistor = {"Band_1": "", "Band_2": "", "Band_3": "", "Band_4": ""}
Five_Band_resistor = {"Band_1": "", "Band_2": "", "Band_3": "", "Band_4": "", "and_5": ""}

def select_resistor_type():
    while True:
        try:
            selected = int(input(f"Choose the resistor type:\n1. 4 Bands\n2. 5 Bands\n: "))
            if selected in [1,2]:
                return resistor_types[selected - 1]
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(e)


def prompt_generate(i, resistor_type):
    prompt = ""
    if i == 0:
        prompt = f"{prompt} {'\n'.join(f'{j}.{color}' for j,color in enumerate(digit_values.keys()) if color != 'Black')}\n"
    elif i == 1:
        prompt = f"{prompt} {'\n'.join(f'{j + 1}. {color}' for j,color in enumerate(digit_values.keys()))}\n"        
    elif i == 2:
        if resistor_type == "4 Bands":
            prompt = f"{prompt} {'\n'.join(f'{j + 1}. {color}' for j,color in enumerate(multiplier_values.keys()))}\n"
        elif resistor_type == "5 Bands":
            prompt = f"{prompt} {'\n'.join(f'{j + 1}. {color}' for j,color in enumerate(digit_values.keys()))}\n"
    elif i == 3:
        if resistor_type == "4 Bands":
            prompt = f"{prompt} {'\n'.join(f'{j + 1}. {color}' for j,color in enumerate(tolerance_values.keys()))}\n"
        elif resistor_type == "5 Bands":
            prompt = f"{prompt} {'\n'.join(f'{j + 1}. {color}' for j,color in enumerate(multiplier_values.keys()))}\n"
    elif i == 4:
        prompt = f"{prompt} {'\n'.join(f'{j + 1}. {color}' for j,color in enumerate(tolerance_values.keys()))}\n"
    return prompt


def enter_4Band_resistor_color():
    color_lists = [color for color in multiplier_values.keys()]
    selected_color = {}
    while True:
        try:
            for i,color in enumerate(Four_Band_resistor):
                selected = int(input(f"Choose the number of the color from \n{prompt_generate(i, "4 Bands")}For Band{i + 1}\n: "))
                if i == 0 and selected - 1 in range(len(digit_values) - 1):
                    selected_color["Band_1"] = color_lists[selected]
                elif i == 1 and selected - 1 in range(len(digit_values)):
                    selected_color["Band_2"] = color_lists[selected - 1]
                elif i == 2 and selected - 1 in range(len(multiplier_values)):
                    selected_color["Multiplier"] = color_lists[selected - 1]
                elif i == 3 and selected - 1 in range(len(tolerance_values)):
                    if selected < color_lists.index("White"):
                        selected_color["Tolerance"] = color_lists[selected]
                    else:
                        selected_color["Tolerance"] = color_lists[selected + 1]
                else:
                    raise ValueError
            return selected_color
        except ValueError:
            print("Invalid Input")
        except Exception as e:
            print(e)
def enter_5Band_resistor_color():
    color_lists = [color for color in multiplier_values.keys()]
    selected_color = {}
    while True:
        try:
            for i,color in enumerate(Five_Band_resistor):
                selected = int(input(f"Choose the number of the color from \n{prompt_generate(i, "5 Bands")}For Band{i + 1}\n: "))
                if i == 0 and selected - 1 in range(len(digit_values) - 1):
                    selected_color["Band_1"] = color_lists[selected]
                elif i == 1 and selected - 1 in range(len(digit_values)):
                    selected_color["Band_2"] = color_lists[selected - 1]
                elif i == 2 and selected - 1 in range(len(digit_values)):
                    selected_color["Band_3"] = color_lists[selected - 1]
                elif i == 3 and selected - 1 in range(len(multiplier_values)):
                    selected_color["Multiplier"] = color_lists[selected - 1]
                elif i == 4 and selected - 1 in range(len(tolerance_values)):
                    if selected < color_lists.index("White"):
                        selected_color["Tolerance"] = color_lists[selected]
                    else:
                        selected_color["Tolerance"] = color_lists[selected + 1]
                else:
                    raise ValueError
            return selected_color
        except ValueError:
            print("Invalid Input")
        except Exception as e:
            print(e)

def four_band_resistor_calculator():
    input_values = enter_4Band_resistor_color()
    first_digit = f"{digit_values[input_values["Band_1"]]}"
    second_digit = f"{digit_values[input_values["Band_2"]]}"
    digits = int(f"{first_digit}{second_digit}")
    multiplier = multiplier_values[f"{input_values["Multiplier"]}"]
    tolerance = tolerance_values[f"{input_values["Tolerance"]}"]
    return f"{digits * multiplier} {tolerance} ohm"

def five_band_resistor_calculator():
    input_values = enter_5Band_resistor_color()
    first_digit = f"{digit_values[input_values["Band_1"]]}"
    second_digit = f"{digit_values[input_values["Band_2"]]}"
    third_digit = f"{digit_values[input_values["Band_3"]]}"
    digits = int(f"{first_digit}{second_digit}{third_digit}")
    multiplier = multiplier_values[f"{input_values["Multiplier"]}"]
    tolerance = tolerance_values[f"{input_values["Tolerance"]}"]
    return f"{digits * multiplier} {tolerance} ohm"
    
calculations = {"4 Bands": four_band_resistor_calculator,
"5 Bands": five_band_resistor_calculator}

resistor_type = select_resistor_type()
print(calculations[resistor_type]())