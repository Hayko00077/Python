# Iterating Through a List with iter() and next(): 
# Write a program that uses iter() and next() to iterate over the list [1, 2, 3, 4, 5] and print each element.

ls = [1, 2, 3, 4, 5]

iterator = iter(ls)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("finish")
print()

# Create an iterator for the string "Python" and print each character one by one using next().
# Stop when you reach the end.

string = "Python"

iterator1 = iter(string)
try:
    while True:
        print(next(iterator1))
except StopIteration:
    pass
print()

#  Write a program that uses iter() and next() to iterate through a list [10, 20, 30, 40] and calculate the sum of its elements.

ls1 = [10, 20, 30 , 40, 50]

iterator2 = iter(ls1)
sum = 0

try:
    for i in range(len(ls1)):
        sum += next(iterator2)
except StopIteration:
    pass
print(sum)
print()

# Use iter() and next() to iterate through [2, 4, 6, 8, 10].
# Stop the iteration manually after printing 3 elements.

ls2 = [2, 4, 6, 8, 10]

iterator3 = iter(ls2)

try:
    for i in range(3):
        print(next(iterator3))
except StopIteration:
    pass
print()

# Given two lists [1, 3, 5] and [2, 4, 6], use iter() and next()
# to alternate between the elements of the two lists and print them in sequence:

ls3 = [1, 3, 5]
ls4 = [2, 4, 6]

iterator4 = iter(ls3)
iterator5 = iter(ls4)

try:
    # for i in range(len(ls3)):
    #     ls4[i] = next(iterator4)
    #     ls3[i] = next(iterator5)
    while True:
        print(next(iterator4))
        print(next(iterator5))
except StopIteration:
    pass

# print(ls3)
# print(ls4)
print()

# Create a list of squares of numbers from 1 to 10 using list comprehension.

squares = [x**2 for x in range(1, 11)]
print(squares)
print()

# Generate a list of even numbers from the range [1, 20] using list comprehension.

even = [num for num in range(1, 21) if num % 2 == 0]
print(even)
print()

# Given a list of words ["python", "list", "comprehension"], create a new list where each word is reversed.

ls5 = ["python", "list", "comprehension"]
reversed_words = [word[::-1] for word in ls5]
print(reversed_words)
print()

# Given a list [1, 2, 3, 4], create a new list where each element is multiplied by 3.

ls6 = [1, 2, 3, 4]
multiplied = [ls6[num] * 3 for num in range(len(ls6))]
print(multiplied)
print()

# Use list comprehension to create a 3x3 matrix (a list of lists) filled with zeros

matrix = [[0 for j in range(3)] for i in range(3)]
for row in matrix:
    print(row)
print()

# Use list comprehension to flatten the following 2D matrix into a single list
# Input: matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
flatten = [elem for row in matrix1 for elem in row]
print(flatten)
print()

# Extract the diagonal elements from a matrix using list comprehension:
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# [1, 5, 9]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal = [matrix2[i][i] for i in range(len(matrix2))]
print(diagonal)

anti_diagonal = [matrix2[i][len(matrix2) - i - 1] for i in range(len(matrix2))]
print(anti_diagonal)

