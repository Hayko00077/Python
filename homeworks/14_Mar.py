# Write a program that prints the numbers from 1 to 100.
# But for multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; for multiples of both 3 and 5, print "FizzBuzz".
# Additionally, for numbers that are prime, print "Prime" instead of the number.

num = 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz") 
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print()

# Create a program that asks the user to enter a password and checks for the following criteria using nested ifs: 
# At least 8 characters long. 
# Contains both uppercase and lowercase letters. Includes at least one numerical digit. 
# Has at least one special character (e.g., !@#$%^&*). If the password doesn't meet any of these criteria, inform the user specifically what is missing.

def check_password(password):
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    else:
        if not any(c.islower() for c in password):
            print("Password must contain at least one lowercase letter.")
            if not any(c.isupper() for c in password):
                print("Password must contain at least one uppercase letter.")
                if not any(c in special_characters for c in password):
                    print("Password must contain at least one special character (e.g., !@#$%^&*).")
            elif not any(c in special_characters for c in password):
                print("Password must contain at least one special character (e.g., !@#$%^&*).")
                if not any(c.isupper() for c in password):
                    print("Password must contain at least one uppercase letter.")
        elif not any(c.isupper() for c in password):
            print("Password must contain at least one uppercase letter.")
            if not any(c.islower() for c in password):
                print("Password must contain at least one lowercase letter.")
                if not any(c in special_characters for c in password):
                    print("Password must contain at least one special character (e.g., !@#$%^&*).")
            elif not any(c in special_characters for c in password):
                print("Password must contain at least one special character (e.g., !@#$%^&*).")
                if not any(c.islower() for c in password):
                    print("Password must contain at least one lowercase letter.")
        elif not any(c in special_characters for c in password):
            print("Password must contain at least one special character (e.g., !@#$%^&*).")
        elif not any(c.isdigit() for c in password):
            print("Password must contain at least one digit")
        else:
            print("Password is valid!")

user_password = input("Enter your password: ")
check_password(user_password)
print()

# Given two 3x3 matrices represented as nested lists, use nested loops to compute and display their product.

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):  
        result[i][j] = matrix1[i][j] * matrix2[i][j]
print("The product of the two matrices is:")
for row in result:
    print(row)
print()

# Given two variables a and b, swap their values using tuple unpacking and without using a temporary variable.

a = 5
b = 10

a, b = b, a
print(f"Swapping a={a} and b={b}")
print()

# Given two lists keys = ['name', 'age', 'city'] and values = ['Alice', 30, 'New York'] 
# use a loop to create a dictionary by assigning elements from keys to corresponding elements in values.

list1 = ['name', 'age', 'city']
list2 = ['Alice', 30, 'New York']
dic = dict()

for i in range(len(list1)):
    dic[list1[i]] = list2[i]
print(dic)