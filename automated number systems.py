# Simple Number System Converter

print("Welcome to Number System Converter!")
print("Supported bases: 2 (binary), 8 (octal), 10 (decimal), 16 (hex)")

# Get the number to convert
number = input("Enter the number: ")

# Get the base of the input number
from_base = int(input("Enter the base of the input number (2, 8, 10, or 16): "))

# Get the base to convert to
to_base = int(input("Enter the base to convert to (2, 8, 10, or 16): "))

# Convert to decimal first
decimal = int(number, from_base)

# Convert from decimal to the target base
if to_base == 2:
    result = bin(decimal)[2:]  # Binary
elif to_base == 8:
    result = oct(decimal)[2:]  # Octal
elif to_base == 10:
    result = str(decimal)  # Decimal
elif to_base == 16:
    result = hex(decimal)[2:].upper()  # Hexadecimal
else:
    result = "Error: Unsupported base"

print(f"The converted number is: {result}")
