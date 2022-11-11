# String syntax: strings in Python can be defined using either single or double quotations
x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y

print("Pluto's a planet!")
print('My dog is named "Pluto"')
# If we try to put a single quote character inside a single-quoted string, Python gets confused

# \n, represents the newline character. It causes Python to start a new line.
hello = "hello\nworld"
print(hello)

# Python's triple quote syntax for strings lets us include newlines literally
triplequoted_hello = """hello world"""
print(triplequoted_hello)
triplequoted_hello = """hello 
world"""
print(triplequoted_hello)
triplequoted_hello == hello

# The print() function automatically adds a newline character 
# unless we specify a value for the keyword argument end other than the default value of '\n'
print("hello")
print("world")
print("hello", end = '') 
print("pluto", end = '\n')
print("hello", end = ' ') 
print("pluto", end = '\n')

# Strings are sequences: Strings can be thought of as sequences of characters. 
# Almost everything we've seen that we can do to a list, we can also do to a string.
# Indexing
planet = 'Pluto'
print (planet[0])

# Slicing
print (planet[-3:])

print (len(planet))

# Yes, we can even loop over them
[char+'! ' for char in planet]

# String methods
# ALL CAPS
claim = "Pluto is a planet!"
claim.upper()

# all lowercase
claim.lower()

# Searching for the first index of a substring
claim.index('plan')

print(claim.startswith(planet))
# planet = 'Pluto'

# false because of missing exclamation mark
print(claim.endswith('planet'))
# claim = "Pluto is a planet!"

# Going between strings and lists: 
# str.split() turns a string into a list of smaller strings, breaking on whitespace by default.
words = claim.split()
print(words)

# Split on something other than whitespace
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)

# str.join() takes us in the other direction, sewing a list of strings up into one long string, 
# using the string it was called on as a separator.
print('/'.join([month, day, year]))

# Building strings with .format()
# Python lets us concatenate strings with the + operator.
planet + ', we miss you.'

# If we want to throw in any non-string objects, we have to be careful to call str() on them first
position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))

# Dictionaries
# Dictionaries are a built-in Python data structure for mapping keys to values.
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])

# Use the same syntax to add another key, value pair
numbers['eleven'] = 11
print(numbers)

# Change the value associated with an existing key
numbers['one'] = 'Pluto'
print(numbers)

# Python has dictionary comprehensions with a syntax similar to  the list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)




