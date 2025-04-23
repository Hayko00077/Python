import typing
from collections.abc import Iterable

# # Tasks on for, if-elif, and Comprehensions ------------------------------------------------------
# # 1. Write a program to identify all prime numbers between 1 and 100 using list comprehensions.

# prime_between_1_to_100 = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
# print(prime_between_1_to_100)

# # 2. Using a list comprehension, create a new list from [1, 2, 3, -4, -5, 6] that contains only the positive numbers.

# ls = [1, 2, 3, -4, -5, 6]
# positive_numbers = [num for num in ls if num > 0]
# print(positive_numbers)

# # 3. Write a program that categorizes numbers in a list as "Even", "Odd", or "Prime" using if-elif inside a loop.

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# categorizes_numbers = ["even" if i % 2 == 0 else "prime" if is_prime(i) else "odd" for i in range(1, 21)]
# print(categorizes_numbers)


# # 4. Create a nested list comprehension to generate a multiplication table (1-10).

# multiplication_table = [[i * j for j in range(1,11)] for i in range(1,11)]
# for row in multiplication_table:
#     print(row)

# # 5. Write a program to filter and print words from a list of strings that start with vowels using list comprehension.

# vowels = ['a', 'e', 'i', 'o', 'u']
# string = "Python is fun. Python is powerful."

# filter_words = [i for i in string.split() if i[0].lower() in vowels]
# print(filter_words)

# # Function Basics ---------------------------------------------------------------
# #6. Write a function calculate_average that takes any number of numerical arguments and returns their average.

# def calculate_average(*args):
#     if len(args) == 0:
#         return 0
#     return sum(args) // len(args)
# average = calculate_average(10, 20, 30, 40, 50)
# print("Average:", average)

# #7. Implement a function reverse_string that accepts a string and returns it reversed without using built-in methods.

# def reverse_string(string):
#     reversed_string = ""
#     for i in range(len(string[::-1])):
#         reversed_string += string[i]
#     return reversed_string
# reversed_str = reverse_string("hello")
# print(reversed_str)

# #8. Write a function personal_greeting that takes a required name argument and an optional greeting argument. The default greeting should be "Hi".

# def personal_greeting(name, greeting = "Hi"):
#     return f"{greeting}, {name}"
# print(personal_greeting("Bob")) 

# #9. Create a function all_greater that takes a list and a number as arguments and checks if all elements in the list are greater than the number.

# def all_greater(ls, number):
#     for i in range(len(ls)):
#         if ls[i] < number:
#             return f"this number {ls[i]} low in this number {number}"
#     return "All good"
# ls1 = [5, 6, 8, 9, 13]
# num = 9
# print(all_greater(ls1, num))

# #10. Write a function divide_numbers that accepts two numbers and returns their division result. Add error handling for division by zero.

# def divide_numbers(num1, num2):
#     try:
#         result = num1 / num2
#         return result
#     except ZeroDivisionError:
#         return "Error: Cannot divide by zero"
# print(divide_numbers(10, 0))

# # Advanced Functions -------------------------------------------------------------------------
# #11. Implement custom_enumerate using yield, similar to the Python built-in enumerate.

# def custom_enumerate(iterable, start = 0):
#     index = start
#     for item in iterable:
#         yield index, item
#         index += 1
# for index, value in custom_enumerate(['apple', 'banana', 'cherry']):
#     print(f"{index} : {value}")
 
# #12. Write a generator function range_generator that mimics the behavior of range(start, stop, step) using yield.

# def range_generator(start, stop, step):
#     current = start
#     while current < stop:
#         yield current
#         current += step
# for num in range_generator(1, 10, 2):
#     print(num)

# #13. Create a function custom_map_with_yield that applies a transformation to elements of an iterable and yields each result.

# def custom_map_with_yield(fn, *iterables):
#     if not isinstance(fn, typing.Callable):
#         raise TypeError("Must be callable")
#     for it in iterables:
#         if not isinstance(it, Iterable):
#             raise TypeError("Arguments need to be Iterable")
#     min_len = min([len(i) for i in iterables])
    
#     for item in range((min_len)):
#         tmp = []
#         for iterable in iterables:
#             tmp.append(iterable[item])
#         yield fn(*tmp)

# res = custom_map_with_yield(lambda x, y:x + y, [1, 2, 3, 4], [1, 6, 5])
# print(list(res))

# #14. Implement custom_filter_with_yield that yields items from an iterable that satisfy a given condition.

# def custom_filter_with_yield(fn, iterable):
#     if not isinstance(fn, typing.Callable):
#         raise TypeError("Must be callable")
#     elif not isinstance(iterable, Iterable):
#         raise TypeError("Arguments need to be Iterable")
#     else:
#         for i in iterable:
#             if fn(i):
#                 yield i
# gen = custom_filter_with_yield(lambda x : x % 2 == 0, [1, 2, 4, 7, 9])
# print(list(gen))

# #15. Write a zip_generator that takes multiple iterables and yields tuples, similar to Python’s zip.

# def zip_generator(*iterables):
#     for it in iterables:
#         if not isinstance(it, Iterable):
#             raise TypeError("Arguments need to be Iterable")
#     min_len3 = min(len(i) for i in iterables)

#     for i in range(min_len3):
#         tmp3 = []
#         for iterable in iterables:
#             tmp3.append(iterable[i])
#         yield tuple(tmp3)
# gen5 = zip_generator([1, 2, 3, 4], ['a', 'b', 'c'])
# print(list(gen5))

# # Closures --------------------------------------------------------------------------------
# # Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.

# def counter():
#     count = 0
#     def wrapper():
#         nonlocal count
#         count += 1
#         return count
#     return wrapper

# x = counter()
# for i in range(3):
#     print(x())

# # Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.

# def multiplier(num):
#     def mul_wrapper(number):
#         res = num * number
#         return res
#     return mul_wrapper
# mul_res = multiplier(5)
# print(mul_res(10))
# print(mul_res(5))

# # Write a closure that tracks the number of times a specific function is called.

# def function_call():
#     count = 0
#     def tracks_wrapper():
#         nonlocal count
#         count += 1
#         print(f"Function called {count} times")
#         return count
#     return tracks_wrapper
# res_call = function_call()
# for i in range(3):
#     res_call()

# # Create a closure to calculate running totals. Each call to the inner function should add a number to the total and return the updated total.

# def calculate_function(num):
#     def calculate(number):
#         nonlocal num
#         num += number
#         return num
#     return calculate
# res_calculate = calculate_function(5)
# print(res_calculate(10))
# print(res_calculate(3))

# # Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.

# def string_manipulator(initial_string=""):
#     current_string = initial_string
#     def string_wrapper(action, text = ""):
#         nonlocal current_string
#         if action == "append":
#             current_string += " " + text
#         elif action == "reset":
#             current_string = ""
#         return current_string
#     return string_wrapper

# manipulate = string_manipulator("Hello")
# print(manipulate("append", "world"))
# print(manipulate("append", "do"))
# print(manipulate("reset"))
