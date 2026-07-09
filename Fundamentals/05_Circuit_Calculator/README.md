# Circuit Calculator

A Python command-line application that performs common electrical engineering calculations used in circuit analysis.

This project was created as part of my **Python Engineering** learning series to strengthen my Python programming skills while applying electrical engineering concepts.


## Features

The calculator currently supports:

* Series Resistance
* Parallel Resistance
* Voltage Divider
* RC Time Constant
* Capacitor Energy
* Inductor Energy
* Capacitive Reactance
* Inductive Reactance
* Resonant Frequency
* Impedance (Reactive)

The program presents an interactive menu, requests only the required inputs for the selected calculation, validates user input, and displays the calculated result.


## Concepts Practiced

### Python

* Functions
* Dictionaries
* Lists
* Loops
* Input validation
* Exception handling (`try` / `except`)
* Dictionary-based function dispatch
* Modular program design
* Floating-point calculations
* Using the `math` module

### Electrical Engineering

* Ohm's Law
* Voltage Divider Rule
* RC Circuits
* Capacitor and Inductor Energy
* Capacitive Reactance
* Inductive Reactance
* Resonant Frequency
* Basic AC Circuit Analysis


## Project Structure

Circuit Calculator
│
├── Menu Selection
├── Input Validation
├── Data Entry Functions
├── Calculation Functions
└── Result Display

Each calculation is implemented in its own function, making the project easy to maintain and extend with additional circuit calculations in the future.


## Example

Choose the calculation you want to make:
1. Series Resistance
2. Parallel Resistance
3. Voltage Divider
4. RC Time Constant
5. Capacitor Energy
6. Inductor Energy
7. Capacitive Reactance
8. Inductive Reactance
9. Resonant Frequency
10. Impedance
10
Enter the value of the resistance(ohm):
12
Enter the value of the inductance(H):
4
Enter the value of the capacitance(F):
5
Enter the value of the frequency(Hz):
1000
Impedance = 12.0 + j25132.741 ohm
|Impedance| = 25132.744 ohm


## What I Learned

This project helped me practice writing larger Python programs by breaking problems into smaller functions, organizing code more effectively, validating user input, and implementing engineering formulas in software. It also reinforced my understanding of several fundamental electrical engineering calculations.
