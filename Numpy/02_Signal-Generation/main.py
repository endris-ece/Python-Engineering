
from enum import Enum
from generators import *
from operators import *

class MainMenu(Enum):
    SIGNAL_GENERATION = 1
    SIGNAL_OPERATION = 2
    EXIT = 3

class SignalGenerationMenu(Enum):
    GENERATE_SINE = 1
    GENERATE_COSINE = 2
    GENERATE_TANGENT = 3
    GENERATE_SQUARE = 4
    GENERATE_EXPONENTIAL = 5
    GENERATE_DAMPED_SINUSOIDAL = 6
    GENERATE_RANDOM = 7
    EXIT = 8

class SignalOperationMenu(Enum):
    ADDITION = 1
    ADD_NOISE = 2
    SCALING = 3
    SHIFTING = 4
    REVERSING = 5
    EXIT = 6


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


def signal_generation(return_signal = False):

    operations = {
        SignalGenerationMenu.GENERATE_SINE: generate_sin,
        SignalGenerationMenu.GENERATE_COSINE: generate_cos,
        SignalGenerationMenu.GENERATE_TANGENT: generate_tan,
        SignalGenerationMenu.GENERATE_SQUARE: generate_square,
        SignalGenerationMenu.GENERATE_EXPONENTIAL: generate_exponential,
        SignalGenerationMenu.GENERATE_DAMPED_SINUSOIDAL: generate_damped_sinusoid,
        SignalGenerationMenu.GENERATE_RANDOM: generate_random,

    }

    option = generate_menu(SignalGenerationMenu)
    while True:
        if return_signal:
            if option == SignalGenerationMenu.EXIT:
                print("Option should not be EXIT!!\n")
                option = generate_menu(SignalGenerationMenu)

            else:
                return operations[option]()
        else:
            if option == SignalGenerationMenu.EXIT:
                break
            else:
                print(operations[option]()["value"])
            option = generate_menu(SignalGenerationMenu)


def signal_operation():

    operations = {
        SignalOperationMenu.ADDITION: signal_addition,
        SignalOperationMenu.ADD_NOISE: add_noise,
        SignalOperationMenu.SCALING: scaling,
        SignalOperationMenu.SHIFTING: amplitude_shifting,
        SignalOperationMenu.REVERSING: reversing,
  
    }

    option = generate_menu(SignalOperationMenu)

    while option != SignalOperationMenu.EXIT:
        try:
                
            if option == SignalOperationMenu.ADDITION:

                signal1 = signal_generation(True)
                signal2 = signal_generation(True)
                if signal1["size"] != signal2["size"] and signal1["time_array"].size != signal2["time_array"].size:
                    raise ValueError("Signal sizes do not match!!")
                
                print(operations[option](signal1["value"], signal2["value"]))
            elif option == SignalOperationMenu.ADD_NOISE:

                signal = signal_generation(True)
                noise_level = float(input("Enter noise level: "))
                print(operations[option](noise_level, signal["value"]))
            elif option == SignalOperationMenu.SCALING:

                scaling_factor = float(input("Enter scaling factor: "))
                signal = signal_generation(True)
                print(operations[option](scaling_factor, signal["value"]))
            elif option == SignalOperationMenu.SHIFTING:

                shifting_factor = float(input("Enter shifting factor: "))
                signal = signal_generation(True)
                print(operations[option](shifting_factor, signal["value"]))
            elif option == SignalOperationMenu.REVERSING:

                signal = signal_generation(True)
                print(operations[option](signal["value"]))

        except ValueError as e:
            print(f"Error: {e}")

        option = generate_menu(SignalOperationMenu)


def start():

    operations = {
        MainMenu.SIGNAL_GENERATION: signal_generation,
        MainMenu.SIGNAL_OPERATION: signal_operation,
  
    }

    option = generate_menu(MainMenu)

    while option != MainMenu.EXIT:
        print(operations[option]())
        option = generate_menu(MainMenu)

start()
