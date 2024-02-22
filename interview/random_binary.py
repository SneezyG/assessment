
"""
--- ALGORITHM:
--- This program first generates a random 4-digit binary number using the generate_binary_number function. Then, it converts the generated binary number to its decimal equivalent using the binary_to_decimal function. Finally, it prints both the random binary number and its decimal equivalent.
"""




import random
import struct


def generate_binary_number():
    binary_number = ""
    for _ in range(4):
        binary_number += str(random.randint(0, 1))
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

# Generate a random binary number
random_binary = generate_binary_number()
print("Random Binary Number:", random_binary)

# Convert binary to decimal(base_10)
decimal_equivalent = binary_to_decimal(random_binary)
print("Base_10 Equivalent:", decimal_equivalent)
