# Importing math from the standard library
import math
print("It's math! It has type {}".format(type(math)))

# math is a module. 
# A module is just a collection of variables (a namespace, if you like) defined by someone else. 
# We can see all the names in math using the built-in function dir().
print(dir(math))

# Access these variables using dot syntax
print("pi to 4 significant digits = {:.4}".format(math.pi))
#  {:n} -> printed element a width of n where n is {:n}

print(math.log(32, 2))

# Other import syntax: 
# The as simply renames the imported module
import math as mt
print(mt.pi)
# It's equivalent to doing something like:
import math
mt = math
# import * makes all the module's variables directly accessible to you (without any dotted prefix).
from math import *
print(pi, log(32, 2))

# Import only the specific things we'll need from each module:
from math import log, pi
from numpy import asarray

# Submodules: contain variables which can refer to functions or values
import numpy
# calling a function in the random "submodule" will require two dots
rolls = numpy.random.randint(low=1, high=6, size=10)
# Roll 10 dice
print(rolls)

# Three tools for understanding strange objects
# type() (what is this thing?):
print(type(rolls))

# dir() (what can I do with it?)
print(dir(rolls))

# If I want the average roll, the "mean" method looks promising...
print(rolls.mean())

# Or maybe I just want to turn the array into a list, in which case I can use "tolist"
print(rolls.tolist())

# help() (tell me more)

# can only concatenate list (not "int") to list
# Cannot concat int to list
# But...
print(rolls + 10)

# At which indices are the dice less than or equal to 3?
print(rolls <= 3)


