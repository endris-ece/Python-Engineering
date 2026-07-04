# Unit Converter

# Description

A command line unit converter that supports conversions for engineering quantities including length, mass, temperature, voltage, current, resistance, capacitance and inductance

# Features
✔ Convert between SI prefixes

✔ Convert length units
    - Meter
    - Kilometer
    - Millimeter
    - Foot
    - Inch
    - Mile

✔ Convert time units
    - Microsecond
    - Millisecond
    - Second
    - Minute
    - Hour

✔ Convert mass
    - Gram
    - Kilogram
    - Pound

✔ Convert temperature
    - Celsius
    - Kelvin
    - Fahrenheit

✔ Convert electrical quantities
    - Voltage
    - Current
    - Resistance
    - Capacitance
    - Inductance

# Concepts Practiced
Python Fundamentals

• Functions
• Lists
• Dictionaries
• Loops
• Conditional statements
• Exception handling
• Input validation
• String formatting
• Code organization
• Modular programming

# Project Structure
Unit_Converter/

├── main.py
└── README.md

# How the program works
The program follows four main steps.

1. Select the engineering quantity.
2. Select the input and output units.
3. Convert the input into a common base unit.
4. Convert the base unit into the requested output unit.

Using a common base unit greatly reduces duplicate conversion logic.

# What i learned
While building this project I learned

• how to organize a larger Python program
• how to avoid duplicated code
• how to use helper functions
• how SI prefixes can be generalized using powers of ten
• how to validate user input