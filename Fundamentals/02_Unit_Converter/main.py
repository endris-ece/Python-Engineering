quantity_list = ["Length", "Time", "Mass", "Temperature", "Voltage", "Current", "Resistance", "Capacitance", "Inductance"]
quantity_units_list = ['Meter', 'Second', 'Gram', 'Kelvin', 'Volt', 'Ampere', 'Ohm', 'Farad', 'Henry']
prefix_dict = {"Pico": -12, "Nano": -9, "Micro": -6, "Milli": -3, "Centi": -2, "Deci": -1,"":0, "Deca": 1, "Hecto": 2, "Kilo": 3, "Mega": 6, "Giga": 9, "Tera": 12}
prefix_list = list(prefix_dict.keys())
time_units_dict = {"MicroSecond": 1000000, "MilliSecond":1000, "Second":1, "Minute": 1/60, "Hour": 1/3600}
temp_units = ["Celsius", "Kelvin", "Fahrenheit"]
quantity_units_dict = {}
FOOT_TO_METER = 0.3048
INCH_TO_METER = 0.0254
MILE_TO_METER = 1609.34
POUND_TO_GRAM = 453.59237
for number in range(len(quantity_list)):
    quantity_units_dict[f"{quantity_list[number]}"] = quantity_units_list[number]

category_prompt = ""
for list_number in range(len(quantity_list)):
    category_prompt =  f"{category_prompt} {list_number + 1}. {quantity_list[list_number]}\n"

#Quantity selection

def select_category():
    exit_loop = False
    while not exit_loop:
        try:
            selected_quantity = int(input(f"Choose the quantity you want to change:\n{category_prompt}: "))
            if selected_quantity - 1 in range(len(quantity_list)):
                exit_loop = True
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid Input, input should be in range (1,{len(quantity_list)})")
        except IndexError:
            print(f"Invalid Input, input should be in range (1,{len(quantity_list)})")

    return selected_quantity

#Unit for the input quantity

def form_quantity_units(category):
    prefix_list = list(prefix_dict.keys())
    category_units = []
    quantity = quantity_list[int(category) - 1]
    if quantity == "Length":
        for prefix in prefix_list:
            category_units.append(f"{prefix}{quantity_units_dict[quantity]}")
        category_units.append("Inch")
        category_units.append("Foot")
        category_units.append("Mile")
    elif quantity == "Time":
        for units in time_units_dict.keys():
            category_units.append(units)
    elif quantity == "Mass":
        for prefix in prefix_list:
            category_units.append(f"{prefix}{quantity_units_dict[quantity]}")
        category_units.append("Pound")
    elif quantity == "Temperature":
        for units in temp_units:
            category_units.append(units)
    else:
        for prefix in prefix_list:
            category_units.append(f"{prefix}{quantity_units_dict[quantity]}")
    
    return category_units

def select_input_unit(category, type = "input"):
    input_prompt = ""
    category_units = form_quantity_units(category)
    for category_unit in category_units:
        input_prompt = f"{input_prompt} {category_units.index(category_unit) + 1}. {category_unit}\n"
    exit_loop = False
    while not exit_loop:
        try:
            input_unit = int(input(f"Select the unit of the {type}:\n{input_prompt}: "))
            if input_unit - 1 in range(len(category_units)):
                exit_loop = True
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid Input, input should be in range (1,{len(quantity_units_list)})")
        except IndexError:
            print(f"Invalid Input, input should be in range (1,{len(quantity_units_list)})")
    return category_units[input_unit - 1]


#Unit for output quantity
def select_output_unit(category, type = "output"):
    return select_input_unit(category, type)

#Input value
def input_value():
    while True:
        try:
            input_value = float(input("Enter Quantity Value: "))
            return input_value
        except ValueError:
            print("Invalid Input Please enter numeric inputs!")


def convert_prefix(number, unit, target):
    unit_prefix = prefix_list[unit]
    target_prefix = prefix_list[target]
    multiplier = prefix_dict[unit_prefix]
    divider = prefix_dict[target_prefix]
    return number * (10**multiplier / (10**divider))

def length_converter(number, unit, target):
    quantity_index = quantity_list.index("Length")
    length_units = form_quantity_units(quantity_index + 1)
    prefix_units = length_units[:len(prefix_list)]
    non_prefix_units = length_units[len(prefix_list):]
    def non_prefix_result(tgt,m_value):
        if target == "Foot":
            return m_value / FOOT_TO_METER
        elif target == "Inch":
            return m_value / INCH_TO_METER
        elif target == "Mile":
            return m_value / MILE_TO_METER
        
    if unit in prefix_units:
        meter_value = convert_prefix(number, length_units.index(unit), length_units.index("Meter"))
        if target in prefix_units:
            result = convert_prefix(number, length_units.index(unit), length_units.index(target))
        else:
            result = non_prefix_result(target, meter_value)
    else:
        if unit == "Foot":
            meter_value = number * FOOT_TO_METER
        elif unit == "Inch":
            meter_value = number * INCH_TO_METER
        elif unit == "Mile":
            meter_value = number * MILE_TO_METER

        result = non_prefix_result(target, meter_value)

    return f"{result} {target}"


def time_converter(number, unit, target):
    divider = time_units_dict[unit]
    multiplier = time_units_dict[target]
    result = number * (multiplier / divider)
    return f"{result} {target}"

def mass_converter(number, unit, target):
    quantity_index = quantity_list.index("Mass")
    mass_units = form_quantity_units(quantity_index + 1)
    if unit == "Pound":
        gram_value = number * 453.59237
    else:
        gram_value = convert_prefix(number, mass_units.index(unit), mass_units.index("Gram"))
    def result(tgt, g_value):
        if tgt == "Pound":
            return g_value/453.59237
        else:
            return convert_prefix(g_value, mass_units.index("Gram"), mass_units.index(tgt))

    result = result(target, gram_value)
    return f"{result} {target}"

def temp_converter(number, unit, target):
    if unit == "Celsius":
        celsius_value = number
    elif unit == "Kelvin":
        celsius_value = number - 273.15
    else:
        celsius_value = (number - 32)*(5/9)

    def result(tgt, c_value):
        if tgt == "Celsius":
            return c_value
        elif tgt == "Kelvin":
            return c_value + 273.15
        else:
            return c_value*(9/5) + 32

    result = result(target, celsius_value)
    return f"{result} {target}"

def other_quantity_converter(number,category, unit, target):
    quantity_index = quantity_list.index(category)
    quantity_units = form_quantity_units(quantity_index + 1)
    result = convert_prefix(number, quantity_units.index(unit), quantity_units.index(target))

    return f"{result} {target}"


ct = select_category()
value = input_value()
input_unit = select_input_unit(ct)
output_unit = select_output_unit(ct)

if quantity_list[int(ct) - 1] == "Length":
    print(length_converter(value, input_unit, output_unit))
elif quantity_list[int(ct) - 1] == "Time":
    print(time_converter(value, input_unit, output_unit))
elif quantity_list[int(ct) - 1] == "Temperature":
    print(temp_converter(value, input_unit, output_unit))
elif quantity_list[int(ct) - 1] == "Mass":
    print(mass_converter(value, input_unit, output_unit))
else:
    print(other_quantity_converter(value, quantity_list[int(ct) - 1], input_unit, output_unit))
