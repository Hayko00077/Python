# # Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.

# def print_down_from_n(n):
#     if n == 0:
#         return 0
#     print(n)
#     return print_down_from_n( n - 1)
# print_down_from_n(10)
# print()

# # Write a function print_characters(s) that prints each character of a string on a new line using recursion.

# def print_characters(s):
#     if len(s) == 0:
#         return 
#     print(s[0])
#     return print_characters(s[1:])
# print_characters("Hello")
# print()

# # Task 1: Calculate Factorial
# # Write a recursive function to calculate the factorial of a number n.
# # Factorial is the product of all positive integers from 1 to n. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# # Input: An integer n >= 0.
# # Output: The factorial of n.
# # Example:
# # Input: n = 5
# # Output: 120
# # Hint:
# # The base case occurs when n = 0 because the factorial of 0 is 1.
# # Use return n * factorial(n-1) to calculate factorial recursively.

# def Calculate_Factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * Calculate_Factorial(n - 1)

# print(Calculate_Factorial(5))
# print()

# # Task 2: Sum of Natural Numbers
# # Create a recursive function to find the sum of the first n natural numbers.
# # The sum of natural numbers from 1 to n is calculated by adding all the numbers in the range.
# # For example, the sum of the first 4 numbers is 1 + 2 + 3 + 4 = 10.
# # Input: An integer n >= 0.
# # Output: The sum of the first n natural numbers.
# # Example:
# # Input: n = 10
# # Output: 55
# # Hint:
# # The base case is when n = 0, and the result is 0.
# # Use return n + sum_natural(n-1) to calculate the sum recursively.

# def Natural_Numbers(n):
#     if n == 0:
#         return 0
#     return n + Natural_Numbers(n - 1)
# print(Natural_Numbers(4))
# print()

# # Task 3: Fibonacci Sequence
# # Write a recursive function to calculate the nth Fibonacci number.
# # The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# # For example, the sequence begins as 0, 1, 1, 2, 3, 5, 8....
# # Input: An integer n >= 0.
# # Output: The nth Fibonacci number.
# # Example:
# # Input: n = 6
# # Output: 8
# # Hint:
# # Base cases: F(0) = 0 and F(1) = 1.
# # Use return fibonacci(n-1) + fibonacci(n-2) for the recursive calculation.

# def Fibonacci_Sequence(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return Fibonacci_Sequence(n - 1) + Fibonacci_Sequence(n - 2)
# print(Fibonacci_Sequence(6))
# print()

# # Task 4: Reverse a String
# # Write a recursive function to reverse a given string.
# # Reversing a string means rearranging its characters from the last to the first.
# # For example, the string "hello" becomes "olleh".
# # Input: A string s.
# # Output: The reversed string.
# # Example:
# # Input: "world"
# # Output: "dlrow"
# # Hint:
# # The base case is when the string is empty (len(s) == 0).
# # Use return s[-1] + reverse_string(s[:-1]) to reverse the string recursively.

# def Reverse_a_String(s):
#     if len(s) == 0:
#         return s
#     else: 
#         return s[-1] + Reverse_a_String(s[:-1])
# print(Reverse_a_String("Hello"))
# print()

# # Task 5: Palindrome Check
# # Write a recursive function to check if a string is a palindrome.
# # A palindrome is a string that reads the same backward as forward. For example, "madam" is a palindrome, but "hello" is not.
# # Input: A string s.
# # Output: True if the string is a palindrome, otherwise False.
# # Example:
# # Input: "racecar"
# # Output: True
# # Hint:
# # The base case is when the string has one or zero characters (len(s) <= 1).
# # Check the first and last characters: if they are equal, recursively check the middle portion of the string (s[1:-1]).

# def Palindrome_Check(s):
#     if len(s) <= 1:
#         return True
#     if s[0] == s[-1]:
#         return Palindrome_Check(s[1:-1])
#     else:
#         return False
# print(Palindrome_Check("racecar"))
# print()

# # Task 6: Power of a Number
# # Write a recursive function to calculate the power of a number x raised to n.
# # For example, 2^4 means multiplying 2 by itself 4 times: 2 * 2 * 2 * 2 = 16.
# # Input: Two integers x (the base) and n (the exponent, n >= 0).
# # Output: The result of x^n.
# # Example:
# # Input: x = 3, n = 3
# # Output: 27
# # Hint:
# # The base case is when n = 0, and the result is 1.
# # Use return x * power(x, n-1) for recursive calculation.

# def power(x, n):
#     if n == 0:
#         return 1
#     print(x * power(x, n - 1))
#     return x * power(x, n - 1)

# x = 3
# n = 3
# result = power(x, n)
# print(result) 
# print()

# # Task 7: Sum of Digits
# # Write a recursive function to calculate the sum of all digits in a number.
# # For example, the digits of 1234 add up to 1 + 2 + 3 + 4 = 10.
# # Input: A positive integer n.
# # Output: The sum of the digits in n.
# # Example:
# # Input: n = 456
# # Output: 15
# # Hint:
# # The base case is when n == 0, and the result is 0.
# # Use return n % 10 + sum_of_digits(n // 10) to extract and add digits recursively.

# def Sum_of_Digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + Sum_of_Digits(n // 10)
# print(Sum_of_Digits(1234))
# print()

# # Task 9: Binary Search
# # Write a recursive binary search algorithm to find the index of a target value in a sorted array.
# # Binary search divides the array into halves to find the target more efficiently.
# # Input: A sorted array arr, its indices low and high, and the target value.
# # Output: The index of the target, or -1 if not found.
# # Example:
# # Input: arr = [2, 4, 6, 8], target = 6
# # Output: 2
# # Hint:
# # Base case: When low > high, return -1.
# # Compare the middle element with the target:
# # If arr[mid] == target, return mid.
# # If arr[mid] > target, search in the left half.
# # Otherwise, search in the right half.

# def Binary_Search(arr, left, right, target):
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return Binary_Search(arr, left, mid - 1, target)
#     else:
#         return Binary_Search(arr, mid + 1, right, target)
# arr = [1, 2, 6, 3]
# target = 6
# low = 0
# high = len(arr) - 1
# print(Binary_Search(arr, low, high, target))
# print()

# # Task 12: Flatten a Nested List
# # Write a recursive function to flatten a list containing nested lists.
# # For example, the list [1, [2, [3, [4]]], 5] should become [1, 2, 3, 4, 5].
# # Input: A list that may contain nested lists.
# # Output: A flattened list with all elements at the same level.
# # Example:
# # Input: [1, [2, [3, [4]]], 5]
# # Output: [1, 2, 3, 4, 5]
# # Hint:
# # The base case is when the list is empty (len(lst) == 0), return an empty list.
# # Check if the first element is a list:
# # If yes, flatten it recursively.
# # If not, add it directly to the result.

# def Flatten_a_Nested_List(ls):
#     if len(ls) == 0:
#         return []
    
#     first = ls[0]
#     print(first)
#     if isinstance(first, list):
#         return Flatten_a_Nested_List(first) + Flatten_a_Nested_List(ls[1:])
#     return [first] + Flatten_a_Nested_List(ls[1:])
# input_list = [1, [2, [3, [4]]], 5]
# output_list = Flatten_a_Nested_List(input_list)
# print(output_list)
# print()

# # Task 13: Find the Maximum Element in a List
# # Write a recursive function to find the maximum element in a list.
# # For example, in the list [3, 1, 4, 1, 5], the maximum element is 5.
# # Input: A non-empty list of integers.
# # Output: The maximum element in the list.
# # Example:
# # Input: [3, 1, 4, 1, 5]
# # Output: 5
# # Hint:
# # The base case is when the list has only one element, which is the maximum.
# # Use return max(lst[0], find_max(lst[1:])) to compare the first element with the maximum of the rest of the list.

# def Find_Max(ls):
#     if len(ls) == 1:
#         return ls[0]
#     return max(ls[0], Find_Max(ls[1:]))
# input_list = [3, 1, 4, 1, 5]
# output = Find_Max(input_list)
# print(output)