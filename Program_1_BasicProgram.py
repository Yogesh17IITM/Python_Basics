# Simple Python program

""" 
Program to demonstrate a simple python program

Concepts:
    How to print?
    Datatypes
"""

#Printing
print("Hello")

#Datatypes (any type it can take)
a = 5               # int
f = 2.25            # float
s = "Hai"           # string
c = 3+4j            # complex
b = True            # bool
binary = 0B0110     # binary
hexadecimal = 0XFF  # Hexadecimal

# Printing all values together
print(a,f,s,c,b, binary, hexadecimal, (9>7))

# to print which data type the member is
print(type(a))
print(type(f))
print(type(c))
print(type(b))
print(type(binary))

# type conversion
var_a = int(f)  # converting float into int
print('Var: ' , var_a)