# # Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
# # Call the function with three numbers.
# # Call the function with no arguments and ensure it handles this case gracefully.

# def sum_numbers(*args):
#     return sum(args)

# print(sum_numbers(1, 2, 3))
# print(sum_numbers())
# print()

# # Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
# # Call the function with keyword arguments such as name="Alice", age=20, and major="CS".
# # Experiment with passing different sets of keyword arguments.

# def display_student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_student_info(name="Alice", age=20, major="CS")
# print()

# # Write a function order_item that accepts:
# # A required item argument.
# # A quantity argument with a default value of 1.
# # Arbitrary positional arguments (*args) to specify additional options.
# # Arbitrary keyword arguments (**kwargs) for customization details.

def order_item(item, quantity=1, *args, **kwargs):
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")

    if args:
        print("Additional options:")
        for option in args:
            print(f"Args value - {option}")
    if kwargs:
        print("Customization details:")
        for key, value in kwargs.items():
            print(f"Kwargs value - {key}: {value}")
order_item(1, 2, 3, 4, x = 5)
print()

# # Write a function register_user that accepts:
# # A required positional argument: username.
# # A required keyword-only argument: email.
# # Hint: Use * to enforce keyword-only arguments.

# def register_user(name, *, email):
#     print(f"User name is: {name}")
#     print(f"User email is: {email}")
# register_user("Hayk", email="vardazaryanhayk7@gmail.com")
# print()

# # Analyze the following code, explain why it raises an error, and fix the function call: 

# # def book_ticket(destination, price = 0, discount=0, *extras, **details):
# #     print(f"Booking to {destination} for ${price - discount}")
# #     if extras:
# #         print(f"Extras: {', '.join(extras)}")
# #     if details:
# #         print(f"Details: {details}")

# # book_ticket("Paris", extras=["window seat", "meal"], discount=10, price=100)


# def book_ticket(destination, price, discount=0, *extras, **details):
#     print(f"Booking to {destination} for ${price - discount}")
#     if extras:
#         print(f"Extras: {', '.join(extras)}")
#     if details:
#         print(f"Details: {details}")

# # book_ticket("Paris", 100, discount=10, "window seat", "meal" , special_request="vegan meal", flight_class="economy")

# # Write a closure that creates a counter.
# # Each call to the inner function should increment the counter by 1 and return the current count.

# def create_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# counter_func = create_counter()
# print(counter_func())
# print(counter_func())
# print(counter_func())
# print()

# # Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.

# def create_multiplier(multiplier):
#     def multiplier_function(x):
#         return x * multiplier
#     return multiplier_function
# multiply_by_5 = create_multiplier(5)

# print(multiply_by_5(5))
# print(multiply_by_5(10))
# print()

# # Write a closure that tracks the number of times a specific function is called.

# def track_calls(func):
#     count = 0 
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"Function {func.__name__} has been called {count} times")
#         return func(*args, **kwargs)
#     return wrapper
# # @track_calls
# def say_hello(string):
#     print(f"Hello {string}")



# say_hello = track_calls(say_hello)

# say_hello("Hayk")
# say_hello("Jor")

# # Implement a function process_data that accepts a mix of positional arguments, default arguments, arbitrary positional arguments (*args), and arbitrary keyword arguments (**kwargs).
# # Require the first two arguments to be data (a list) and operation (a string that specifies the operation to perform: 'sum', 'multiply', 'filter').
# # Optionally accept a threshold parameter with a default value of None. This will only be used for the 'filter' operation.
# # Accept additional numbers via *args to be appended to the data list before processing.
# # Accept additional processing options through **kwargs, such as:
# # reverse (boolean): Whether to reverse the result.
# # unique (boolean): Whether to ensure the data list contains unique values before processing.
# # Function Behavior:
# # If the operation is 'sum', return the sum of the elements in the data list.
# # If the operation is 'multiply', return the product of the elements in the data list.
# # If the operation is 'filter', return a list of numbers greater than threshold.
# # Apply reverse and unique options based on the kwargs values.

# def process_data(data, operation, threshold = None, *args, **kwargs):
#     if not isinstance(data, list):
#         raise TypeError("Data should be type of list !!!")
#     if operation not in ("sum", "multiply", "filter"):
#         raise ValueError("Accept only this operation sum, multiply, filter")
    
#     data.extend(args)
#     result = data
#     print(result)

#     if operation == "sum":
#         result = sum(result)
#     elif operation == "multiply":
#         mul = 1
#         for i in range(len(result)):
#             mul *= result[i]
#         result = mul
#     elif operation == "filter":
#         if not threshold:
#             raise ValueError("Threshild should not be None!!!")
#         result = [i for i in result if i > threshold]

#     if kwargs.get("unique", False):
#         if isinstance(result, list):
#             return len(set(result)) == len(result)
#     if kwargs.get("reverse", False):
#         if isinstance(result, int):
#             tmp = 0
#             while result:
#                 tmp = tmp * 10 + result % 10
#                 result //= 10
#             result = tmp
#         elif isinstance(result, list):
#             result.reverse()
#     return result

# print(process_data([1, 2, 3], "filter", 1, 4, 5, reverse=True))
