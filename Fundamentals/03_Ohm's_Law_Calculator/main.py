quantity_units = {"Voltage" : "Volt", "Current" : "Ampere", "Resistance" : "Ohm"}
quantity_list = [{"Quantity":key,"Unit": value} for key, value in quantity_units.items()]

prompt = ""
for i, item in enumerate(quantity_list):
    prompt = f"{prompt}{i+1}. {item['Quantity']}\n"

def select_toBeCalculated_unit():
    while True:
        try:
            toBeCalculated = int(input(f"Enter the quantity you want to calculate:\n{prompt}"))
            if toBeCalculated in range(1,len(quantity_list) + 1):
                return quantity_list[toBeCalculated - 1]
            print(f"Choose a number between 1 and {len(quantity_list)}")

        except ValueError:
            print(f"Input should be in range (1,{(len(quantity_list))})")


def enter_parameters(target):
    input_quantity = [q for q in quantity_list if q != target]
    while True:
        try:
            input_values = {}
            for quantity in input_quantity:
                input_value = float(input(f"Enter {quantity['Quantity']} ({quantity['Unit']}): "))
                if input_value >= 0:
                    input_values[quantity["Quantity"]] = input_value
                else:
                    raise ValueError
            return input_values
        except ValueError:
            print("Invalid Input, Values should be numeric and non-negative")

def calculate(input_values, target):
    calculations = {
    "Voltage": lambda d: d["Current"] * d["Resistance"],
    "Current": lambda d: d["Voltage"] / d["Resistance"],
    "Resistance": lambda d: d["Voltage"] / d["Current"],}
    try:
        result = calculations[target["Quantity"]](input_values)
        return f"{target['Quantity']} = {result:.2f} {target['Unit']}"
    except ZeroDivisionError:
        if target["Quantity"] == "Current" and input_values["Resistance"] == 0:
            return "Resistance cannot be zero."

        if target["Quantity"] == "Resistance" and input_values["Current"] == 0:
            return "Current cannot be zero."        

target = select_toBeCalculated_unit()
input_lists = enter_parameters(target)
print(calculate(input_lists, target))