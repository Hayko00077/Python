from functools import wraps
import time

# # Write a decorator greet_decorator that adds a greeting message before and after the execution of the decorated function.

# def greet_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         func(*args, **kwargs)
#         print("Goodbye")
#     return wrapper


# @greet_decorator
# def say_name(): 
#     print("My name is Python.")
# say_name()
# print()

# # Create a decorator log_execution that logs the name of the function being executed along with its arguments and return value.

# def log_execution(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Executing {func.__name__} with arguments (args = {args} and kwargs = {kwargs})")
#         res = func(*args, **kwargs)
#         print(f"{func.__name__} returned {res}")
#     return wrapper

# @log_execution
# def add(a, b):
#     return a + b
# add(4, 5)
# print()

# # Write a decorator execution_timer that measures and prints the time taken by the decorated function to execute.

# def execution_timer(func):
#     @wraps(func)
#     def wrraper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         print(f"{func.__name__} took {time.time() - start:.2f} seconds to execute")
#     return wrraper

# @execution_timer
# def slow_function(): 
#     time.sleep(2) 
#     print("Finished execution!")
# slow_function()
# print()

# # Create a decorator require_login that only allows a function to execute if a global variable is_logged_in is True. If not, raise an exception.

# is_logged_in = False

# def require_login(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if is_logged_in:
#             func(*args, **kwargs)
#         else:
#             raise TypeError("Can not access user")
#     return wrapper

# @require_login 
# def view_profile(): 
#     print("Accessing user profile...")
# view_profile()
