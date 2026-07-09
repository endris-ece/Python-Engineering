import math

calculation_lists = ["Series Resistance",
"Parallel Resistance",
"Voltage Divider",
"RC Time Constant",
"Capacitor Energy",
"Inductor Energy",
"Capacitive Reactance",
"Inductive Reactance",
"Resonant Frequency",
"Impedance"]

def select_calculator():
    prompt = ""
    for i, calc in enumerate(calculation_lists):
        prompt = f"{prompt}{i + 1}. {calc}\n"
    while True:
        try:
            selected_calc = int(input(f"Choose the calculation you want to make:\n{prompt}"))
            if selected_calc in range(1, len(calculation_lists) + 1):
                return calculation_lists[selected_calc - 1]
            else:
                raise ValueError
            return result
        except ValueError:
            print(f"Invalid Input, values should be in range {range(1, len(calculation_lists))}")
        except Exception as e:
            print(e)

def enter_resistance_values():
    input_values = []
    while True:
            try:
                input_value = float(input("Enter the valus of the resistors, when you finish enter 0\n"))
                if input_value == 0:
                    return input_values
                elif input_value < 0:
                    print(f"Negative resistance value is not allowed")
                elif input_value > 0:
                    input_values.append(input_value)
                else:
                    raise ValueError
            except ValueError:
                print(f"Invalid input, please try again")
            except Exception as e:
                print(e)
def enter_voltage_divider_values():
    while True:
        try:
            input_voltage = float(input("Enter the value of the input voltage(V):\n"))
            resistance1 = float(input("Enter the value of the resistance R1(ohm):\n"))
            resistance2 = float(input("Enter the value of the resistance R2(ohm):\n"))
            if input_voltage > 0 and resistance1 > 0 and resistance2 > 0:
                result = {"input_voltage":input_voltage, "resistance1": resistance1, "resistance2": resistance2}
            else:
                raise ValueError
            return result
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)

def enter_capacitor_energy_values():
    while True:
        try:
            capacitance = float(input("Enter the value of the capacitance of the capacitor(F):\n"))
            voltage_value = float(input("Enter the value of the voltage(V):\n"))
            if capacitance > 0 and voltage_value > 0:
                result = {"capacitance": capacitance, "voltage": voltage_value}
            else:
                raise ValueError
            return result
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)

def enter_inductor_energy_values():
    while True:
        try:
            inductance = float(input("Enter the value of the inductance of the inductor(H):\n"))
            current_value = float(input("Enter the value of the current(A):\n"))
            if inductance > 0 and current_value > 0:
                result = {"inductance":inductance,"current": current_value}
            else:
                raise ValueError
            return result        
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)

def enter_rc_time_constant_values():
    while True:
        try:
            resistance = float(input("Enter the value of the resiatnce(ohm):\n"))
            capacitance = float(input("Enter the value of the capacitance(F):\n"))
            if resistance> 0 and capacitance > 0:
                result = {"resistance": resistance, "capacitance":capacitance}
            else:
                raise ValueError
            return result         
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)

def enter_capacitive_reactance_values():
    while True:
        try:
            capacitance = float(input("Enter the value of the capacitance(F):\n"))
            frequency = float(input("Enter the value of the frequency(Hz):\n"))
            if capacitance > 0 and frequency > 0:
                result = {"capacitance":capacitance, "frequency": frequency}
            else:
                raise ValueError   
            return result         
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)

def enter_inductive_reactance_values():
    while True:
        try:
            inductance = float(input("Enter the value of the inductance(H):\n"))
            frequency = float(input("Enter the value of the frequency(Hz):\n"))
            if inductance > 0 and frequency > 0:
                result = {"inductance":inductance, "frequency": frequency}
            else:
                raise ValueError
            return result         
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)


def enter_resonant_frequency_values():
    while True:
        try:
            inductance = float(input("Enter the value of the inductance(H):\n"))
            capacitance = float(input("Enter the value of the capacitance(F):\n"))
            if inductance > 0 and capacitance > 0:
                result = {"inductance": inductance, "capacitance": capacitance}
            else:
                raise ValueError
            return result
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)

def enter_impedance_values():
    while True:
        try:
            resistance = float(input("Enter the value of the resistance(ohm):\n"))
            inductance = float(input("Enter the value of the inductance(H):\n"))
            capacitance = float(input("Enter the value of the capacitance(F):\n"))
            frequency = float(input("Enter the value of the frequency(Hz):\n"))
            if resistance > 0 and inductance > 0 and capacitance > 0 and frequency > 0:
                result = {"resistance": resistance, "inductance": inductance, "capacitance": capacitance, "frequency": frequency}
            else:
                raise ValueError
            return result
        except ValueError:
            print(f"Invalid input, please try again")
        except Exception as e:
            print(e)         

def parallel_resistance_calculator():
    input_values = enter_resistance_values()
    total = 0
    for value in input_values:
        total = total + 1/value
    result = 1/total
    return f"Equivalent resistance = {result:.3f} ohm"

def series_resistance_calculator():
    input_values = enter_resistance_values()
    total = 0
    for value in input_values:
        total = total + value
    result = total
    return f"Equivalent resistance = {result:.3f} ohm"

def voltage_divider_calculator():
    input_values = enter_voltage_divider_values()
    v_out1 = input_values["resistance1"]*input_values["input_voltage"]/(input_values["resistance1"] + input_values["resistance2"])
    v_out2 =  input_values["resistance2"]*input_values["input_voltage"]/(input_values["resistance1"] + input_values["resistance2"])
    return f"Volatge across R1({input_values["resistance1"]}) = {v_out1:.3f} volt\nVoltage across R2({input_values["resistance2"]}) = {v_out2:.3f} volt"

def rc_time_constant_calculator():
    input_values = enter_rc_time_constant_values()
    time_constant = (input_values["capacitance"]*input_values["resistance"])
    return f"Tau = {time_constant:.3f} sec"

def capacitor_energy_calculator():
    input_values = enter_capacitor_energy_values()
    energy = (input_values["capacitance"] * (input_values["voltage"]**2))/2
    return f"Capacitor Energy = {energy:.3f} Joules"

def inductor_energy_calculator():
    input_values = enter_inductor_energy_values()
    energy = (input_values["inductance"] * (input_values["current"]**2))/2
    return f"Inductor Energy = {energy:.3f} Joules"
    
def capacitive_reactance_calculator():
    input_values = enter_capacitive_reactance_values()
    reactance = 1/(2* math.pi *(input_values["capacitance"]*input_values["frequency"]))
    return f"Reactance = {reactance:.3f} ohm"

def inductive_reactance_calculator():
    input_values = enter_inductive_reactance_values()
    reactance = 2*math.pi * (input_values["frequency"]*input_values["inductance"])
    return f"Reactance = {reactance:.3f} ohm"

def resonant_frequency_calculator():
    input_values = enter_resonant_frequency_values()
    resonant_frequency = 1/(2*math.pi *(math.sqrt(input_values["capacitance"]*input_values["inductance"])))
    return f"Resonant Frequency = {resonant_frequency:.3f} Hz"

def impedance_calculator():
    input_values = enter_impedance_values()
    reactive_impedance = 1/(2*math.pi *(input_values["capacitance"]*input_values["frequency"]))
    inductive_impedance = 2*math.pi * (input_values["frequency"]*input_values["inductance"])
    impedance = inductive_impedance - reactive_impedance
    magnitude = math.sqrt(input_values["resistance"]**2 + impedance**2)
    return f"Impedance = {input_values["resistance"]} + j{impedance:.3f} ohm\n|Impedance| = {magnitude:.3f} ohm"

calculations = {"Series Resistance": series_resistance_calculator,
"Parallel Resistance": parallel_resistance_calculator,
"Voltage Divider": voltage_divider_calculator,
"RC Time Constant": rc_time_constant_calculator,
"Capacitor Energy": capacitor_energy_calculator,
"Inductor Energy": inductor_energy_calculator,
"Capacitive Reactance":capacitive_reactance_calculator,
"Inductive Reactance": inductive_reactance_calculator,
"Resonant Frequency": resonant_frequency_calculator,
"Impedance": impedance_calculator}


calculator = select_calculator()
output = calculations[calculator]()
print(output)
