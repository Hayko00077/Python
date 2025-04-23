# # 1. Implementing filter
# # Task: Write a Python function named custom_filter that replicates the behavior of the built-in filter function.
# # Your implementation should take two arguments:
# # A function that returns a boolean value.
# # An iterable.

# import typing

# def my_filter(function, iterable):
#     result = []
#     if function is None:
#         for i in iterable:
#             if i:
#                 result.append(i)
#     if not isinstance(function, typing.Callable) and function is not None:
#         raise TypeError("Error!!!!!!!")
#     for i in iterable:
#         if function(i):
#             result.append(i)
#     return result

# def is_even(n):
#     return n % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_number = my_filter(is_even, numbers)
# print(even_number)
# print()

# # 2. Implementing map
# # Task: Write a Python function named custom_map that replicates the behavior of the built-in map function. Your implementation should take two arguments:
# # A function that transforms an input.
# # An iterable.
# # The function should return a list where each item is the result of applying the function to the corresponding item in the iterable.

# def my_map(function, *iterables):
#     min_len = len(min(iterables, key=len))
#     result1 = []
#     for i in range(min_len):
#         tmp = []
#         for iter in iterables:
#             tmp.append(iter[i])
#         result1.append(function(*tmp))
#     return result1

# def square(x):
#     return x ** 2

# numbers1 = [1, 2, 3, 4]
# square_numbers = my_map(square, numbers1)
# print(square_numbers)
# print()

# # 3. Implementing zip
# # Task: Write a Python function named custom_zip that replicates the behavior of the built-in zip function.
# # Your implementation should take two iterables and return a list of tuples, where each tuple contains one element from each iterable at the same position.
# # Requirements:
# # Ensure the returned list is as long as the shorter of the two input iterables.
# # Use a loop to pair elements from the iterables into tuples.

# def my_zip(*iterables):
#     min_len = len(min(iterables, key=len))
   
#     result3 = []
#     for i in range(min_len):
#         tmp1 = []
#         for j in iterables:
#             tmp1.append(j[i])
#         result3.append(tuple(tmp1))
#     return result3

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# res_zip = my_zip(list1, list2)
# print(res_zip)
# print()

# # 4. Implementing reduce
# # Task: Write a Python function named custom_reduce that replicates the behavior of the functools.reduce function.
# # Your implementation should take three arguments:
# # A binary function (takes two inputs).
# # An iterable.
# # An optional initializer (default is None).
# # The function should apply the binary function cumulatively to the items in the iterable, reducing it to a single value.

# def my_reduce(function, iterables):
#     num = 0
#     for i in iterables:
#         num = function(i, num)
#     return num
    

# def add(x, y):
#     return x + y

# numbers4 = [1, 2, 3, 4]
# add_numbers = my_reduce(add, numbers4)
# print(add_numbers)
# print()

# # 5. Implementing enumerate
# # Task: Write a Python function named custom_enumerate that replicates the behavior of the built-in enumerate function.
# # Your implementation should take two arguments:
# # An iterable.
# # An optional starting index (default is 0).
# # The function should return a list of tuples, where each tuple contains an index (starting from the given starting index) and the corresponding item from the iterable.
# # Requirements:
# # Use a loop to generate the index and pair it with the corresponding item.
# # Append the index-item pairs as tuples to a new list.
# # Return the list.

# def my_enumerate(iterables, start = 0):
#     result5 = []
#     index = start
#     for i in iterables:
#         result5.append((index, i))
#         index += 1
#     return result5
# fruits = ['apple', 'banana', 'cherry']
# fruits_res = my_enumerate(fruits, start=1)
# print(fruits_res) 