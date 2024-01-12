def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:].upper()

def binary_to_decimal(binary):
    return int(binary, 2)

def octal_to_decimal(octal):
    return int(octal, 8)

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def normalize_binary(binary):
    return format(int(binary, 2), '0' + str(len(binary)) + 'b')

def normalize_octal(octal):
    return format(int(octal, 8), '0' + str(len(octal)) + 'o')

def normalize_hexadecimal(hexadecimal):
    return format(int(hexadecimal, 16), '0' + str(len(hexadecimal)) + 'X')

def convert_number(number, from_base, to_base):
    decimal = 0
    if from_base == 'binary':
        decimal = binary_to_decimal(number)
    elif from_base == 'octal':
        decimal = octal_to_decimal(number)
    elif from_base == 'hexadecimal':
        decimal = hexadecimal_to_decimal(number)
    else:
        decimal = int(number)

    if to_base == 'binary':
        return normalize_binary(decimal_to_binary(decimal))
    elif to_base == 'octal':
        return normalize_octal(decimal_to_octal(decimal))
    elif to_base == 'hexadecimal':
        return normalize_hexadecimal(decimal_to_hexadecimal(decimal))
    else:
        return str(decimal)

def main():
    print("Welcome to the number system converter!")
    print("Supported number systems: binary, octal, decimal, hexadecimal")
    print("Enter 'exit' to quit the program.")

    while True:
        number = input("Enter a number: ")
        if number == 'exit':
            break

        from_base = input("Enter the base of the number: ")
        to_base = input("Enter the base to convert to: ")

        converted_number = convert_number(number, from_base, to_base)
        print(f"Converted number: {converted_number}\n")

if __name__ == '__main__':
    main()
