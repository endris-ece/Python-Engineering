class NumberSystem:
    
    def __init__(self, name, rep, base, digits):
        self.name = name
        self.rep = rep
        self.base = base
        self.digits = digits
        
binary_digits = ["0", "1"]
octal_digits = ["0", "1", "2", "3", "4", "5", "6", "7"]
decimal_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
hex_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
hex_digits_dict = {"0":0, "1":1,"2":2, "3":3, "4":4, "5":5,"6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

number_system_list = [
NumberSystem("Binary","1", 2, binary_digits),
NumberSystem("Octal", "2", 8, octal_digits),
NumberSystem("Decimal", "3", 10, decimal_digits),
NumberSystem("Hexa-Decimal", "4", 16, hex_digits)
]

prompt = ""
number_system_dict = {number_system.rep: number_system for number_system in number_system_list}
for key in number_system_dict.keys():
    prompt = f"{prompt}\n{key}. {number_system_dict[key].name}"

# Input Number System 

exit_loop = False
while not exit_loop:
    input_number_system = input(f"Which number system is the input in: {prompt}\n: ")
    if input_number_system in [number_system.rep for number_system in number_system_list]:
        exit_loop= True
    else:
        print("Invalid Input, input should be between 1 and 4")


#The number to be converted

exit_loop = False
while not exit_loop:
    input_number = input("Enter the number to be converted: ")
    for number in input_number:
        exit_loop = False
        if number not in number_system_dict[input_number_system].digits:
            print(f"Invalid Input, values should be in {number_system_dict[input_number_system].digits}")
            break
        else:
            exit_loop = True

  
#Output number system

exit_loop = False
while not exit_loop:
    output_number_system = input(f"Choose the target number system: {prompt}\n")
    if output_number_system in [number_system.rep for number_system in number_system_list]:
        exit_loop= True
    else:
        print("Invalid Input, input should be between 1 and 4")

#Decimal number system to any other number system converter

def to_decimal(number, number_sys_multiplier):
    decimal = 0
    msb_exp = len(number) - 1
    nsm = int(number_sys_multiplier)

    for bits in number:
        digit = hex_digits_dict[bits]
        decimal = decimal + (digit *(nsm**msb_exp))
        msb_exp -= 1

    return decimal


#Decimal number system to any other number system converter

def decimal_converter(number, target):
    integer_form = int(number)
    output_bits = []
    output = ""
    exit_loop = False
    while not exit_loop:
        remainder = integer_form % number_system_dict[target].base
        quotient = integer_form // number_system_dict[target].base
        integer_form = quotient
        digit = hex_digits[remainder]
        output_bits.insert(0, digit)
        if quotient == 0:
            exit_loop = True

    for bits in output_bits:
        output = output + f"{bits}"
    return output
        

def convert(number, initial, target):
    decimal_eqv = to_decimal(number, number_system_dict[initial].base)
    if target == "3":
        return decimal_eqv
    else:
        return decimal_converter(decimal_eqv, target)


#system calling
print(convert(input_number, input_number_system, output_number_system))