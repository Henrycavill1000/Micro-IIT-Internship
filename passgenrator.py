import random
import string
low = string.ascii_lowercase
upp = string.ascii_uppercase
numbers = string.digits
specialsymbols = string.punctuation

len = int(input("Enter the length of the password: "))
input_low = input("any lowercase letters (type yes or no): ").lower()=='yes'
input_upp = input("any uppercase letters (type yes or no): ").lower()=='yes'
input_num = input("any digits (type yes or no): ").lower()=='yes'
input_special = input("any special characters (type yes or no): ").lower()=='yes'
totalcharacters = ""

if input_low:
    totalcharacters += low
if input_upp:
    totalcharacters += upp
if input_num:
    totalcharacters += numbers
if input_special:
    totalcharacters += specialsymbols
if not totalcharacters:
    print("Please type yes or no in the input. (Error)")
    exit()
password = ''.join(random.choice(totalcharacters) for _ in range(len))
print("generated password = ", password)