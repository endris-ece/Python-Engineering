
import numpy as np

rng = np.random.default_rng()

def enter_parameters():

    while True:
        try:

            frequency = float(input("Enter frequency(Hz): "))
            amplitude = float(input("Enter amplitude: "))
            phase = np.deg2rad(float(input("Enter phase angle: ")))
            minimum = int(input("Enter minimum of sampling range: "))
            maximum = int(input("Enter maximum of sampling range: "))
            amount = int(input("Enter sample amount: "))

            if frequency < 0:
                raise ValueError("Frequency can't be negative!!\n")
            
            if 0 >= maximum - minimum or maximum - minimum > 100:
                raise ValueError("Sampling range should be in (0, 100]!!\n")

            
            if 0 >= amount or amount > 10000:
                raise ValueError("Sample amount should be in (0, 10000]!!\n")

            return {"frequency": frequency, "amplitude": amplitude, "phase": phase, "minimum": minimum, "maximum": maximum, "amount": amount}
        except ValueError as e:
            print(e)


def generate_sin():

    parameters = enter_parameters()
    t = np.linspace(parameters["minimum"], parameters["maximum"], parameters["amount"])
    value = parameters["amplitude"]*np.sin(2*np.pi*parameters["frequency"]*t + parameters["phase"])
    value = np.round(value, 6)
    return {"value": value,"time_array": t, "size": parameters["amount"]}


def generate_cos():

    parameters = enter_parameters()

    t = np.linspace(parameters["minimum"], parameters["maximum"], parameters["amount"])

    value = parameters["amplitude"]*np.cos(2*np.pi*parameters["frequency"]*t + parameters["phase"])
    value = np.round(value, 6)
    return {"value": value,"time_array": t, "size": parameters["amount"]}


def generate_tan():

    parameters = enter_parameters()

    t = np.linspace(parameters["minimum"], parameters["maximum"], parameters["amount"])

    value = parameters["amplitude"]*np.tan(2*np.pi*parameters["frequency"]*t + parameters["phase"])
    value = np.round(value, 6)
    return {"value": value,"time_array": t, "size": parameters["amount"]}


def generate_square():

    parameters = enter_parameters()

    t = np.linspace(parameters["minimum"], parameters["maximum"], parameters["amount"])

    value = parameters["amplitude"]*np.sign(np.sin(2*np.pi*parameters["frequency"]*t + parameters["phase"]))
    value = np.round(value, 6)
    return {"value": value,"time_array": t, "size": parameters["amount"]}


def generate_exponential():

    while True:
        try:

            amplitude = float(input("Enter initial amplitude: "))
            alpha = float(input("Enter exponential growth/decay rate: "))
            minimum = int(input("Enter minimum of sampling range: "))
            maximum = int(input("Enter maximum of sampling range: "))
            amount = int(input("Enter sample amount: "))

            if 0 >= maximum - minimum or maximum - minimum > 100:
                raise ValueError("Sampling range should be in (0, 100]!!\n")

            
            if 0 >= amount or amount > 10000:
                raise ValueError("Sample amount should be in (0, 10000]!!\n")

            break
        except ValueError as e:
            print(e)

    t = np.linspace(minimum, maximum, amount)

    value = amplitude*np.exp(alpha*t)
    value = np.round(value, 6)
    return {"value": value,"time_array": t, "size": amount}

def generate_damped_sinusoid():

    while True:
        try:
            parameters = enter_parameters()

            alpha = float(input("Enter exponential growth/decay rate: "))

            break
        except ValueError as e:
            print(e)

    t = np.linspace(parameters["minimum"], parameters["maximum"], parameters["amount"])

    value = parameters["amplitude"]*np.exp(alpha*t)*np.cos(2*np.pi*parameters["frequency"]*t + parameters["phase"])
    value = np.round(value, 6)
    return {"value": value,"time_array": t, "size": parameters["amount"]}


def generate_random():

    while True:
        try:

            minimum = int(input("Enter minimum of sampling range: "))
            maximum = int(input("Enter maximum of sampling range: "))
            amount = int(input("Enter sample amount: "))

            if 0 >= maximum - minimum or maximum - minimum > 100:
                raise ValueError("Sampling range should be in (0, 100]!!\n")

            
            if 0 >= amount or amount > 10000:
                raise ValueError("Sample amount should be in (0, 10000]!!\n")

            break
        except ValueError as e:
            print(e)

    t = np.linspace(minimum, maximum, amount)
    random_signal = rng.uniform(-1, 1, amount)

    return {"value": random_signal,"time_array": t, "size": amount}


