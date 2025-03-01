# Write a program that prompts the user to create an empty list.
# Then, the user should be able to add elements to the list using three different methods: 
# append(), extend(), and insert().
##########
ls = []
ls.append(4)
ls.extend([1, 2, 3])
ls.insert(2,7)
print(ls)
print()

# Extend the previous program to allow the user to remove elements using two methods: 
# remove() and pop().

ls1 = [1, 2, 3, 4, 5]
ls1.remove(3)
ls1.pop(2)
print(ls1)
print()

# Write a program that prompts the user to create a list containing different types of elements
# (integers, strings, floating-point numbers, etc.). 
# Allow the user to add elements of different types to the list using append(), extend(), and insert().

ls2 = [1, 2.4, 'hello']
ls2.append('world')
ls2.extend([6, 7.5, 'apple'])
ls2.insert(3, 5)
print(ls2)
print()

# Write a program to create a list and a tuple with some elements.
# Print them and display their types.

ls3 = [1, 2, 3, 4]
tp = (1, 2, 3, 4)
print(f"list",ls3)
print(f"tuple",tp)
print(type(ls3))
print(type(tp))
print()

# Write a program to count the occurrences of a specific element in a list and tuple.

count = 0
count1 = 0
x = int(input("Enter the number: "))
ls4 = [1, 2, 3, 4, 5, 1, 2, 3, 5]
tp1 = (1, 2, 3, 4, 5, 1, 2, 3, 5)
for i in range(0, len(ls4)):
    if x == ls4[i]:
        count += 1
for i in range(0, len(tp1)):
    if x == tp1[i]:
        count1 += 1
print(f"in list: ",count)
print(f"in tiple: ",count1)
print()

# Write a program to find and print the maximum and minimum values in a list and a tuple.

tp2 = (1, 2, 3, 4, 5, 8, 6)
max_val = tp2[0]
min_val = tp2[0]

for i in range(1, len(tp2)):
    if max_val < tp2[i]:
        max_val = tp2[i]
    if min_val > tp2[i]:
        min_val = tp2[i]
print(f"maximum value is {max_val} and minimum value is {min_val}")
print()

# Write a program to access elements from a nested list and a nested tuple.

ls5 = [1, 2, [4, 5, 6], (8, 9)]
ls5[2][1] = 10
print(ls5[3][0])
print(ls5)
print()

# Write a program to find the sum of all elements in a list and a tuple.

sum_list = 0
sum_tuple = 0
ls6 = [1, 2, 3, 4, 5]
tp3 = (1, 2, 3, 4)

for i in range(0, len(ls6)):
    sum_list += ls6[i]

for i in range(0, len(tp3)):
    sum_tuple += tp3[i]

print(f"Sum of list elements {sum_list} and Sum of tuple elements {sum_tuple}")
print()

# Write a program to reverse a list and a tuple.

ls7 = [1, 2, 3, 4, 5]
tp4 = (5, 4, 3, 2, 1)

ls7.reverse()
y = list(tp4)
y.reverse()
tp4 = tuple(y)
print(f"Reversed list {ls7}\t and\t Reversed tuple {tp4}")
print()

# Create a program that adds, subtracts, multiplies, and divides two integers, two floats, 
# and a combination of both.

sym = input("Enter the symbol to do arithmetic operator (-, +, *, /): ")
num1 = 10
num2 = 5
float_num1 = 10.5
float_num2 = 5.4

match sym:
    case "-":
        print("operations_on_integers", num1 - num2)
    case "+":
        print("operations_on_integers", num1 + num2)
    case "*":
        print("operations_on_integers", num1 * num2)
    case "/":
        print("operations_on_integers", num1 // num2)
print()
match sym:
    case "-":
        print("operations_on_floats", float_num1 - float_num2)
    case "+":
        print("operations_on_floats", float_num1 + float_num2)
    case "*":
        print("operations_on_floats", float_num1 * float_num2)
    case "/":
        print("operations_on_floats", float_num1 / float_num2)
print()
match sym:
    case "-":
        print("operations_on_mixed", num1 - float_num2)
    case "+":
        print("operations_on_mixed", num1 + float_num2)
    case "*":
        print("operations_on_mixed", num1 * float_num2)
    case "/":
        print("operations_on_mixed", num1 / float_num2)
print()

# Write a program to calculate the product of two complex numbers.

complex_num1 = complex(3, 5)
complex_num2 = complex(4, 6)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed!"
def operations_on_complex_numbers(a, b):
    print(f"Adding: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")

operations_on_complex_numbers(complex_num1, complex_num2)
print()

# Create a fraction that represents 1/2 and another fraction representing 2/3. 
# Add them and print the result.

from fractions import Fraction

fraction_num1 = Fraction(1, 2)
fraction_num2 = Fraction(2, 3)

print(f"Adding", fraction_num1 + fraction_num2)
print()

# Using decimal, calculate the sum of 0.1 and 0.2 and compare it with float.

from decimal import Decimal

decimal_num1 = Decimal(0.1)
decimal_num2 = Decimal(0.2)
res1 = decimal_num1 + decimal_num2

float_number1 = 0.1
float_number2 = 0.2
res2 = float_number1 + float_number2

print(res1 == res2)
print()

# Write a program to check if the sum of three numbers is equal to 100. 
# Use boolean comparisons to print the result as True or False.

number1 = int(input("Enter the first number to check with 100: "))
number2 = int(input("Enter the second number to check with 100: "))
tmp = 100
print(tmp == number1 + number2)
print()

# Accept two fractions from the user (in the form of a/b where both a and b are integers) and multiply them. 
# Use the fractions.Fraction class to handle fractions and print the resulting fraction in its simplified form.

def get_fraction_input(prompt):
    fraction_str = input(prompt)

    numerator, denominator = map(int, fraction_str.split('/'))
    return Fraction(numerator, denominator)


fraction1 = get_fraction_input("Enter the first fraction (in the form a/b): ")
fraction2 = get_fraction_input("Enter the second fraction (in the form a/b): ")

result3 = fraction1 * fraction2
print(result3)

# Accept two fractions from the user and find their GCD using the math.
# gcd() function along with the numerator and denominator attributes of each fraction.

import math
def get_fraction_input(prompt):
    fraction_str1 = input(prompt)
    numerator, denominator = map(int, fraction_str1.split('/'))
    return Fraction(numerator, denominator)

fraction3 = get_fraction_input("Enter the first fraction (in the form a/b): ")
fraction4 = get_fraction_input("Enter the second fraction (in the form a/b): ")

gcd_numerator = math.gcd(fraction3.numerator, fraction4.numerator)
gcd_denominator = math.gcd(fraction3.denominator, fraction4.denominator)

print(f"The GCD of the numerators is: {gcd_numerator}")
print(f"The GCD of the denominators is: {gcd_denominator}")

gcd_fraction = Fraction(gcd_numerator, gcd_denominator)
print(f"The GCD of the two fractions is: {gcd_fraction}")
print()

# Write a program to check if a number is even or odd.

num5 = int(input("Enter the number: "))
if num5 % 2:
    print("Number is odd")
else:
    print("Number is even")
print()

# Compare the values of a float and an int and print whether they are equal or not.

num6 = 10
float_num6 = 10.0

print(num6 == float_num6)
print()

# Calculate the square of an integer and a float using the exponentiation operator (**).

num7 = 10
float_num7 = 5.7

print(f"Integer {num7 ** 2} and float {float_num7 ** 2}")
print()

# Write a program to find the maximum of three numbers using nested conditional operators.

num8 = float(input("Enter the first number: "))
num9 = float(input("Enter the second number: "))
num10 = float(input("Enter the third number: "))

max_num3 = num8 if (num8 > num9 and num8 < num10) else (num9 if num9 < num10 else num10)
print(max_num3)

# Accept two integer inputs from the user and calculate the absolute difference between them using the abs() function. 
# Print the result.

num11 = int(input("Enter the first number: "))
num12 = int(input("Enter the second number: "))

difference = abs(num11 - num12)

print("The absolute difference between", num11, "and", num12, "is:", difference)
print()

# Accept an integer input from the user and use conditional statements to 
# print whether the number is positive, negative, or zero.

num13 = int(input("Enter the number: "))

if num13 > 0:
    print("The number is positive")
elif num13 < 0:
    print("The number is negative")
else:
    print("Nummber is zero")
print()

# Accept two integer inputs from the user. 
# Check if the first number is a multiple of the second and print True if it is, otherwise print False.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 != 0 and num1 % num2 == 0:
    print(True)
else:
    print(False)