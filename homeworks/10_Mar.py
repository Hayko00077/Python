# Write a function named greet that prints "Hello, World!". Call the function. 

def greet():
    print("Hello World")
greet()
print()

# Write a function add that takes two numbers as arguments and returns their sum. 
# Call the function with different inputs.

def add_two_num(a, b):
    sum = a + b
    return sum
x = add_two_num(4, 5)
print(x)
print()

# Create a function multiply that takes two numbers and returns their product.

def multiply_two_num(a, b):
    multiply = a * b
    return multiply
x1 = multiply_two_num(4, 5)
print(x1)
print()

# Write a function personal_greet that takes a name as an argument and prints "Hello, [name]!".

def personal_greet(name):
    print(f"Hello {name}")
personal_greet("Hayk")
print()

# Write a function calculate_area that takes length and width as parameters and returns the area of a rectangle.
# print(calculate_area(5, 10))

def calculate_area(length, width):
    rectangle = length * width
    return rectangle
x2 = calculate_area(5, 3)
print(x2)
print()

# Write a function greet_with_message that takes a name and an optional message.
# The default message should be "Welcome!".

def greet_with_message(name, string):
    print(f"Welcome! {name} {string}")
name1 = "Jor"
st = "How are you"
greet_with_message(name1, st)
print()

# Write a function power that takes a number and an optional exponent.
# The default exponent should be 2 (square the number).

def power(number, exponent = 2):
    res = number ** exponent
    return res
x3 = power(5)
print(x3)
print()

# Write a program with a global variable x.
# Create a function that changes the value of x inside the function and prints both the global and local values.

digit = 5

def changes():
    digit = 10
    print(digit)
changes()
print("Global digit", digit)
print()

# Write a function is_even that takes a number and returns True if the number is even and False otherwise.

def is_even(num):
    if num % 2:
        return False
    else:
        return True
output = is_even(4)
print(output)
print()


# Write a function find_max that takes two numbers and returns the larger of the two.

def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
x4 = find_max(5, 6)
print(x4)
print()

# Write a function calculate_discount that takes a price and a discount percentage and returns the discounted price.

def calculate_discount(price, discount):
    discount_amount = price * (discount / 100)
    discounted_price = price - discount_amount
    return discounted_price
x5 = calculate_discount(10, 5)
print(x5)
print()

# Write a function filter_positive that takes a list of numbers and returns a new list containing only the positive numbers.

def filter_positive(ls : list):
    ls1 = []
    for i in range(len(ls)):
        if ls[i] > 0:
            ls1.append(ls[i])
    return ls1
ls = [1, 2, 3, -1, 5, -6]
new_list = filter_positive(ls)
print(new_list)
print()

# Write a function count_digits that takes an integer and returns the number of digits in it.

def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
x6 = count_digits(123123)
print(x6)
print()

# Write a function sum_of_digits that calculates the sum of all digits in an integer

def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
x6 = sum_of_digits(153)
print(x6)