# Create a program that extracts the first 5 characters from a given string.

string = "helloworld"
substring = string[:5]
print("First 5 character", substring)
print()

# Extract the last 3 characters of a string using slicing.

string1 = "helloworld"
substring1 = string1[-3:]
print("Last 3 character", substring1)
print()

# Write a program to print every second character from a string.

string2 = "hello world"
for i in range(0, len(string2), 2):
    print(string2[i])
print()

# Reverse a given string using slicing and print the result.

string3 = "hello"
reversed_string = string3[::-1]
print("Reversed string", reversed_string)
print()

# Replace all occurrences of a specific character with another character in a string.

string4 = "hello world"
ls2 = list(string4)
ls2[2] = "k"
string4 = ''.join(ls2)
print(string4)
print()

# Write a program to print a formatted message like: 
# "Hello, my name is James and I am 20 years old." using f-strings.

name = "James"
age = 20
print(f"Hello, my name is {name} and I am {age} years old")
print()

# Create a program to format and print a float with 2 decimal places.

number = float(input("Enter a float number: "))
print(f"{number:.2f}")
print()

# Write a program to convert all characters in a string to uppercase and then to lowercase.

string5 = "Hello world"
Upper_string = string5.upper()
Lower_string = string5.lower()

print(f"Upper <{Upper_string}>\tand\tLower <{Lower_string}>")
print()

# Create a program to count the number of occurrences of a specific character in a string.

string6 = "hello world"
count = string6.count("o")
print("Count of character", count)
print()

# Write a program to concatenate two strings with a space in between.

string7 = "hello"
string8 = "world"

print(string7 + " " + string8)
print()

# Create a program to find the sum of the first and last digit of a given number.

number1 = 1234
ls3 = list(str(number1))
print(f"sum of the first and last digits", int(ls3[0]) + int(ls3[-1]))
print()

# Write a program to calculate the average of 3 float numbers
# and format the result to 3 decimal places.

number2 = float(input("Enter the first float number: "))
number3 = float(input("Enter the second float number: "))
number4 = float(input("Enter the third float number: "))

avarage = (number2 + number3 + number4) / 3

print(f"{avarage:.3f}")
print()

# Create a program that takes a string input and an integer input
# and repeats the string that many times.

import time
number5 = int(input("Enter the number how many times want see string: "))
string9 = input("Enter the string: ")

for i in range(number5):
    print(string9)
    time.sleep(1)
print()

# Ask the user to enter a string, and then print the string in reverse order.

string10 = input("Enter the string to reverse: ")
reversed_string10 = ''.join(reversed(string10))
print("Reversed string", reversed_string10)
print()

# Count how many vowels are in the string and print the count.

string11 = "HELLO world"
vowels = "aeiou"
vowel_count = 0

for char in string11:
    if char.lower() in vowels:
        vowel_count += 1
print("Vowel count in string", vowel_count)
print()

# Write a program that takes a string as input and outputs the longest 
# substring without repeating characters. For example, the string 
# "abcabcbb" should return "abc".

def longest_substring(s: str) -> str:

    start = 0
    char_index_map = {}
    max_length = 0
    longest_substr = ""

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1

        char_index_map[s[end]] = end
    
        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substr = s[start:end+1]

    return longest_substr

string12 = input("Enter the string: ")
print(longest_substring(string12))

# Write a program using a while loop that repeatedly asks the user to input a number until they input 0, 
# then print the sum of all entered numbers.

sum = 0

while True:
    number6 = int(input("Enter the number if you want finish enter <0> "))
    sum += number6
    if number6 == 0:
        print("finished")
        break
print("Sum of the numbers", sum)
print()

# Create a list of 10 numbers (hardcoded) and calculate the sum of all numbers in the list.

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum1 = 0
for i in ls:
    sum1 += i
print("Sum of list elements", sum1)
print()

# Declare a list and print the value of the maximum of the elements in the list. 
# The list must contain only int values. Do not use the max function.

ls1 = [1, 2, 35, 12, 45]
max_val = ls1[0]

for i in range(0, len(ls1)):
    if max_val < ls1[i]:
        max_val = ls1[i]
print("Maximum dighit in list", max_val)
print()

# Declare a list and print the index of the element with the minimum value.

ls2 = [23, 4, 5, 6, 2, 66]
min_val = ls2[0]
min_index = 1

for i in range(0, len(ls2)):
    if min_val > ls2[i]:
        min_val = ls2[i]
        min_index = i
print("Minimum dighit index in the list", min_index)
print()

# Declare two lists with integer values ​​and print the product of the elements with corresponding indices to the screen.

ls3 = [1, 2, 3, 4, 5]
ls4 = [6, 7, 8, 9, 10]
ls5 = []
for i in range(0, len(ls3)):
    ls5.append(ls3[i] * ls4[i])
print("the product of the elements with corresponding indices to the screen.", ls5)
print()

# Write a program that receives an integer. Declare a list. 
# If the given number is in the list, print YES, otherwise print NO.

ls6 = [1, 2, 3, 4, 5, 6]
number6 = int(input("Enter the searching number: "))
for i in range(len(ls6)):
    if number6 == ls6[i]:
        print("Yes")
        break
else:
    print("No")
print()

# Declare a list consisting of strings. Print how many times each occurs in the list.

ls7 = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]

for i in ls7:
    print(f"{i} occurs {ls7.count(i)} times")
