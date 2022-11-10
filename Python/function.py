# Defining functions
# Creates a function called least_difference, which takes three arguments, a, b, and c.
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3) 

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), 
    # Python allows trailing commas in argument lists. 
)

help(least_difference)

# Docstrings : Python isn't smart enough to read my code and turn it into a nice English description. 
#              We can provide a description in what's called the docstring.
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    # The docstring is a triple-quoted string (which may span multiple lines) 
    # that comes immediately after the header of a function
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3) 

# Functions that don't return: Python allows us to define such functions. 
# The result of calling them is the special value None. 
# (This is similar to the concept of "null" in other languages.)
def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    min(diff1, diff2, diff3)

# Print:
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)

mystery = print()
print(mystery)

# Default arguments: 
# The print function has several optional arguments:
print(1, 2, 3, sep=' < ')
print(1, 2, 3)

# Adding optional arguments with default values to the functions we define turns out to be pretty easy:
def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")

# Functions Applied to Functions:
# Supply functions as arguments to other functions
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

# Functions that operate on other functions are called "higher-order functions.
# max returns the largest of its arguments. But if we pass in a function using the optional key argument, 
# it returns the argument x that maximizes key(x)
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key = mod_5),
    sep='\n',
)