
from enum import Enum
from signal_statistics import *

class MainMenu(Enum):
    BASIC_STATISTICS = 1
    SIGNAL_ANALYSIS = 2
    EXIT = 3

class BasicStatisticsMenu(Enum):
    MEAN = 1
    MEDIAN = 2
    MODE = 3
    STANDARD_DEVIATION = 4
    VARIANCE = 5
    MINIMUM = 6
    MAXIMUM = 7
    RANGE = 8
    EXIT = 9

class SignalAnalysisMenu(Enum):
    PEAK_AMPLITUDE = 1
    PEAK_TO_PEAK = 2
    RMS = 3
    ENERGY = 4
    AVERAGE_POWER = 5
    PERCENTILE = 6
    EXIT = 7


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

def generate_signal():
    while True:
        try:
                
            signal = []
            n = int(input("Enter the number of elements in the signal: "))

            if n <= 0:
                raise ValueError("Number of elements must be a positive integer!!\n")

            for _ in range(n):
                element = float(input("Enter an element: "))
                signal.append(element)
            return signal
        except ValueError as e:
            print(e)

def basic_statistics():

    operations = {
        BasicStatisticsMenu.MEAN: mean,
        BasicStatisticsMenu.MEDIAN: median,
        BasicStatisticsMenu.MODE: mode,
        BasicStatisticsMenu.STANDARD_DEVIATION: standard_deviation,
        BasicStatisticsMenu.VARIANCE: variance,
        BasicStatisticsMenu.MINIMUM: minimum,
        BasicStatisticsMenu.MAXIMUM: maximum,
        BasicStatisticsMenu.RANGE: find_range
    }

    option = generate_menu(BasicStatisticsMenu)

    while option != BasicStatisticsMenu.EXIT:
        signal = generate_signal()
        print(operations[option](signal))
        option = generate_menu(BasicStatisticsMenu)


def signal_analysis():

    operations = {
        SignalAnalysisMenu.PEAK_AMPLITUDE: peak_amplitude,
        SignalAnalysisMenu.PEAK_TO_PEAK: peak_to_peak,
        SignalAnalysisMenu.RMS: rms,
        SignalAnalysisMenu.ENERGY: energy,
        SignalAnalysisMenu.AVERAGE_POWER: average_power,
        SignalAnalysisMenu.PERCENTILE: percentile,
    }

    option = generate_menu(SignalAnalysisMenu)

    while option != SignalAnalysisMenu.EXIT:
        if option == SignalAnalysisMenu.PERCENTILE:
            p = float(input("Enter the percentile (0-100): "))
            operations[option] = lambda s, p=p: percentile(s, p)
        signal = generate_signal()
        print(operations[option](signal))
        option = generate_menu(SignalAnalysisMenu)


def start():

    operations = {
        MainMenu.BASIC_STATISTICS: basic_statistics,
        MainMenu.SIGNAL_ANALYSIS: signal_analysis,
    }

    option = generate_menu(MainMenu)

    while option != MainMenu.EXIT:
        print(operations[option]())
        option = generate_menu(MainMenu)

start()
