# # 1. Simple Number Sequence Generator
# # Objective
# # Familiarize students with creating a basic generator function using the yield keyword.
# # Practice iterating over a generator with a for loop or next() calls.

# def Generator_Sequence(n):
#     for i in range(1, n + 1):
#         yield i
# for number in Generator_Sequence(5): # 1 example
#     print(number)

# gen = Generator_Sequence(5)
# print(next(gen))
# print(next(gen))  #2 example
# print()

# # 2. Write a generator function called simple_sequence(start, end)
# # that takes two integers (start and end) and yields each integer from start to end (inclusive).

# def simple_sequence(start, end):
#     for i in range(start, end + 1):
#         yield i
# for number in simple_sequence(3, 7):
#     print(number)
# print()

# # 3. Test the generator by iterating over it and printing each value.

# def foo(n):
#     for i in range(1, n + 1):
#         yield i
# for number in foo(5):
#     print(number)
# print()

# # 4. Handle the scenario where start might be greater than end (in which case, the generator should yield nothing).

# def range_check(start, end):
#     if start > end:
#         return
#     elif start <= end:
#         for i in range(start, end + 1):
#             yield i
# print("Test 1: start <= end")
# for value in range_check(1, 5):
#     print(value)

# print("\nTest 2: start > end")
# for value in range_check(6, 5):
#     print(value)
# print()

# # 5. Countdown Generator with Print Statements
# # Objective
# # Understand how generator functions suspend and resume using yield.
# # See the order of execution with print statements.
# # Task
# # Write a generator function countdown(n) that starts at n and counts down to 1, yielding each number.
# # Print a message like "Yielding: X" before each yield so students can visualize the flow.
# # Demonstrate the generator by calling next() several times manually (instead of a loop) to see how the function suspends and resumes.

# def countdown(n):
#     while (n):
#         print(f"Yielding: {n}")
#         yield n  
#         n -= 1

# for i in countdown(5):
#     print(i)
# print()

# # 6. Generator Expression for Data Transformation
# # Objective
# # Introduce generator expressions (parentheses syntax).
# # Compare and contrast list comprehensions vs. generator expressions.
# # Task
# # Create a list of integers: numbers = list(range(1, 11)).
# # Use a list comprehension to create squares_list (the square of each number).
# # Use a generator expression to create squares_gen.
# # Print both squares_list and then iterate over squares_gen. Observe how squares_gen does not store all items in memory at once.

# list_numbers = list(range(1, 11))

# squares_list = [x ** 2 for x in list_numbers]
# print("Squares List (List Comprehension):")
# print(squares_list)

# squares_gen = (x ** 2 for x in list_numbers)
# print("\nSquares Generator (Generator Expression):")
# for i in squares_gen:
#     print(i)
# print()

# # 7. Fibonacci Generator (Intermediate)
# # Objective
# # Introduce a slightly more complex logic to generate a well-known sequence.
# # Reinforce lazy evaluation: only generate the next Fibonacci number upon request.
# # Task
# # Write a generator function fibonacci(limit=None) that yields Fibonacci numbers.
# # If limit is not given (None), generate an infinite sequence. Otherwise, stop once the next Fibonacci number would exceed limit.
# # Demonstrate by printing the first 10 Fibonacci numbers (or all Fibonacci numbers up to a certain limit if provided).

# def Fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# for i in Fibonacci(6):
#     print(i)
# print()

# # 8. Even Numbers Generator
# # Objective
# # Practice filtering logic within a generator.
# # Reinforce the idea of yielding only certain values (in this case, even numbers).
# # Task
# # Write a generator function even_numbers(nums) that takes a list (or any iterable) of integers and yields only those that are even.
# # Test it on a small list of mixed even/odd integers.
# # Print each yielded value to confirm it’s even.

# def Even_Number(n):
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             yield i

# for i in Even_Number(11):
#     print(i)
# print()

# 9. Cumulative Sum Generator
# Objective
# Create a generator that computes and yields partial sums.
# Illustrate maintaining state (running total) within a generator.
# Task
# Write a generator function cumulative_sum(nums) that takes a list (or any iterable) of numbers.
# As you iterate through each number, keep adding it to a running total and yield the new total each time.
# Test it on a small list, printing each partial sum.

# def cumulative_sum(nums):
#     num = 0
#     for i in range(len(nums)):
#         num += nums[i]
#         yield num

# numbers_list = [1, 3, 5, 2]
# for partial_sum in cumulative_sum(numbers_list):
#     print(partial_sum)
