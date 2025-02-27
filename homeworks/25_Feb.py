# # Write a Python program that asks the user for two numbers and prints their sum.

x = 4
y = 8
print(x + y)
print()

# # Create two integer variables and perform addition, subtraction, multiplication, and division.

x2 = 4
y2 = 6
print(f"Adding:", x2 + y2)
print(f"Subtraction:", x2 - y2)
print(f"Multiplication:", x2 * y2)
print(f"Division:", x2 // y2)
print()

h = 3.5
k = 4.6
print(f"Adding:", h + k)
print(f"Subtraction:", h - k)
print(f"Multiplication:", h * k)
print(f"Division:", h / k)
print()

a = 3 + 4j
b = 5 + 3j

print(f"Adding:", a + b)
print(f"Subtraction:", a - b)
print(f"Multiplication:", a * b)
print(f"Division:", a / b)
print()


# Create and Compare Numbers of Different Types
# Compare an integer and a float
# Compare a decimal and a float
# Compare two fractions

from decimal import Decimal
from fractions import Fraction

integer_value = 7
float_value = 10.6

print("Comparing Integer and Float:")
print("Is integer equal to float?", integer_value == float_value)
print("Is integer greater than float?", integer_value > float_value)
print("Is integer less than float?", integer_value < float_value)
print()

decimal_value = Decimal(10.5)
print("Comparing Decimal and Float:")
print("Is integer equal to float?", decimal_value == float_value)
print("Is integer greater than float?", decimal_value > float_value)
print("Is integer less than float?", decimal_value < float_value)
print()

fraction1 = Fraction(2, 5)
fraction2 = Fraction(2, 9)
print("Comparing 2 Fraction numbers:")
print("Is fraction1 equal to fraction2?", fraction1 == fraction2)
print("Is fraction1 greater than fraction2?", fraction1 > fraction2)
print("Is fraction1 less than fraction2?", fraction1 < fraction2)
print()


# Create Complex Numbers and Calculate Magnitude
# Create two fractions and perform addition, subtraction, multiplication, and division manually. Afterward, check the results using Python.
# Create a decimal number and experiment with adding or subtracting very small decimal values.

complex_number = complex(3, 5)
complex_number2 = complex(6, 5)

real_number = complex_number.real
imag_number = complex_number.imag
real_number2 = complex_number2.real
imag_number2 = complex_number2.imag

Magnitude = (real_number ** 2 + imag_number ** 2) ** 0.5
Magnitude2 = (real_number2 ** 2 + imag_number2 ** 2) ** 0.5

print(f"Magnitude first number:", Magnitude)
print(f"Magnitude second number:", Magnitude2)
print()


from fractions import Fraction
from decimal import Decimal

fraction3 = Fraction(2, 5)
fraction4 = Fraction(2, 9)

print(f"Adding:", fraction3 + fraction4)
print(f"Subtraction:", fraction3 - fraction4)
print(f"Multiplication:", fraction3 * fraction4)
print(f"Division:", fraction3 / fraction4)
print()


decimal_val = Decimal(10.5)
decimal_val2 = Decimal(4.3)

print(f"Adding:", decimal_val + decimal_val2)
print(f"Subtraction:", decimal_val - decimal_val2)
print()


# Create examples to compare two numbers using all relational operators
# (>, <, ==, !=, >=, <=). Write down the results for different types of numbers.

num1 = 29
num2 = 10

print("First number greater:", num1 > num2)
print("Second number greater:", num1 < num2)
print("Two numbers are equal:", num1 == num2)
print("Two numbers are not equal:", num1 != num2)
print("First number greater or equal to second number", num1 >= num2)
print("Second number greater or equal to first number", num1 <= num1)
print()


num3 = 10.25
num4 = 4.7

print("First number greater:", num3 > num4)
print("Second number greater:", num3 < num4)
print("Two numbers are equal:", num3 == num4)
print("Two numbers are not equal:", num3 != num4)
print("First number greater or equal to second number", num3 >= num4)
print("Second number greater or equal to first number", num3 <= num4)
print()


# Create two separate strings and then concatenate them together. 
# Have them experiment with adding a space between the words.

string1 = "hello"
string2 = "world"
result = string1 + " " + string2
print(result)
print()


# Write a program that takes a string and extracts the first 
# and last character using subscripts (indexing).

string = "hello world"
char1 = string[0]
char2 = string[len(string) - 1]
print(f"first character {char1} and last character {char2}")
print()


# Write a program that slices the first 3 characters and the last 2 characters from a string.

input = "Python"

output = input[:3]
output1 = input[-2:]
print(output + " and " + output1)
print()


# Write a program that takes two strings as input and concatenates them with a space in between.

tmp = "Good"
tmp1 = "Morning"

resilt4 = tmp + " " + tmp1
print(resilt4)
print()


# Write a program that takes a string and converts it to both uppercase and lowercase.

input1 = "Hello World"

Upper = input1.upper()
Lower = input1.lower()

print(f"{Upper} and {Lower}")
print()


# Write a program that checks whether a string starts with the letter "A" 
# and ends with the letter "Z".

srt = "AmazingZ"

if srt[0] == "A" and srt[len(srt) - 1] == "Z":
    print("Starts with A: True, Ends with Z: True")
elif srt[0] == "A" and srt[len(srt) - 1] != "Z":
    print("Starts with A: True, Ends with Z: False")
elif srt[0] != "A" and srt[len(srt) - 1] == "Z":
    print("Starts with A: False, Ends with Z: True")
else:
    print("Starts with A: False, Ends with Z: False")
    print()


# Write a program that counts how many times the letter "a" appears in a given string.

temp = "banana"

count = temp.count('a')
print(count)
print()

# Write a program that takes a sentence and splits it into words, 
# then joins the words back into a sentence with hyphens (-) between them.

st = "i love python"
word = st.split()
print(word)
new_word = "-".join(word)
print(new_word)
print()


# Write a program that takes a user’s name as input 
# and creates a greeting message like "Hello, [Name]!".

st2 = str(input("Enter the name"))

print(f"Hello {st2}")
