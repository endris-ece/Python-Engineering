# Truth Table Generator

## Overview

The Truth Table Generator is a Python-based program that generates truth tables for common digital logic gates.

The user selects a logic gate and specifies the number of inputs (for multi-input gates). The program automatically generates all possible input combinations and calculates the corresponding output for each combination.

This project was created to strengthen understanding of:

* Digital logic fundamentals
* Boolean algebra
* Binary number representation
* Python functions and dictionaries
* Algorithm design



## Supported Logic Gates

The program supports the following gates:

* NOT
* AND
* OR
* NAND
* NOR
* XOR
* XNOR



## Features

### Automatic Input Combination Generation

The program generates all possible binary input combinations based on the number of inputs.

For `n` inputs:


Number of combinations = 2^n

Example for 3 inputs:

A B C
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1


### Multiple Input Support

Multi-input gates are supported.

The user can select between 2 and 10 inputs.

Example:

Enter the number of inputs:
3


The program generates:

A   B   C   | Output

0   0   0   | 0
0   0   1   | 0
0   1   0   | 0
0   1   1   | 1
1   0   0   | 0
1   0   1   | 1
1   1   0   | 1
1   1   1   | 1


## Project Structure

Truth_Table_Generator/
│
├── truth_table_generator.py
└── README.md


## Concepts Practiced

This project applies the following Python concepts:

* Variables and data types
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* Function mapping using dictionaries
* Binary number conversion logic

