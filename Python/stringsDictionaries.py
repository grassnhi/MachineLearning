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

claim.startswith(planet)

# Building strings with .format()
# Python lets us concatenate strings with the + operator.
planet + ', we miss you.'

# If we want to throw in any non-string objects, we have to be careful to call str() on them first
position = 9
planet + ", you'll always be the " + position + "th planet to me."


