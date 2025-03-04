# Write a program that takes a sentence and creates a dictionary
# where each word is a key, and the value is the number of times that word appears.
# Use a sample sentence and break it into words to fill the dictionary. 

string = "Python is fun, and Python is powerful! Python, fun, fun."

ls = string.split()
dic = {}

for word in ls:
    if word[-1] in ",.!?":
        word = word[:-1]
    word = word.lower()
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
print(dic)
print()

# Create a dictionary to store student names as keys and their scores as values.
# Use a few sample names and scores to populate the dictionary. 
# Print out each student’s name and score on a new line.

string2 = {
    "Bob" : 23,
    "James" : 85,
    "Tom" : 90,
    "Thomas" : 100
}

for name, score in string2.items():
    print(f"{name} : {score}")
print()


# Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}). 
# Use this dictionary to convert a list of numbers into words and print each word on a new line.

ls1 = ["one", "two", "three", "four", "five"]
dic1 = {}

for i in range(1, len(ls1) + 1):
    dic1[i] = ls1[i - 1]
print(dic1)
print()

# Create a dictionary to represent a store’s inventory with items as keys and quantities as values. 
# Print the quantity of a specific item (e.g., "Apples").
# Update the quantity of an item and print the dictionary to show the change.

ls2 = ["apple", "banana", "orange", "kiwi"]
count = 30
dic2 = {}

for i in ls2:
    dic2[i] = 10
for i in dic2:
    dic2[i] += count
    count += 10
print(dic2)
print()

# Write a program that takes a sentence and uses a set to find all unique words.
# Print each unique word on a new line.

string3 = "apple banana apple orange apple grape banana orange apple"

st = set(string.split())
for i in range(len(st)):
    print(i)
print()

# Given two lists of numbers, use sets to find and print the common elements between them.

ls3 = [1, 2, 3, 4, 5, 6 , 7 ,8]
ls4 = [1, 2, 5, 7, 9]

st1 = (set(ls3) & set(ls4))
print(st1)

# Given a list of numbers, use a set to find any duplicates in the list and print them.
# You can add numbers to a set one by one and check if they are already present.
# Example: For the list [1, 2, 2, 3, 4, 4, 5], the output should be {2, 4}.

ls5 = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set()
duplicates = set()

for i in ls5:
    if i in unique_numbers:
        duplicates.add(i)
    else:
        unique_numbers.add(i)
print(duplicates)
print()

# Use a set to create a list of vocabulary words from a paragraph. 
# Break the paragraph into individual words, add each word to the set, and print the final set of unique words.
# Example: For the paragraph "Python is fun. Python is powerful.", the output should be {"Python", "is", "fun", "powerful"}.

string4 = "Python is fun. Python is powerful."
ls6 = list(set(string4.split()))
for i in range(len(ls6)):
    if ls6[i][-1] in ",.!?":
        ls6[i] = ls6[i][:-1]
print(ls6)