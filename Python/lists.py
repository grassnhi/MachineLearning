# Lists in Python represent ordered sequences of values
primes = [2, 3, 5, 7]

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

# Indexing: You can access individual list elements with square brackets.
planets[0]
planets[1]

# Elements at the end of the list can be accessed with negative numbers, starting from -1:
planets[-1]
planets[-2]

# Slicing: What are the first three planets? 
planets[0:3]

# The starting and ending indices are both optional. 
# If I leave out the start index, it's assumed to be 0
planets[:3]

# If leaving out the end index, that number will be assumed to be the length of the list.
planets[3:]

# All the planets except the first and last
planets[1:-1]

# The last 3 planets
planets[-3:]

# Changing lists: Lists are "mutable", meaning they can be modified "in place".
planets[3] = 'Malacandra'
planets

# Let's compensate by shortening the names of the first 3 planets.
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

# Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
print(planets)

# List functions:
# len gives the length of a list:
len(planets)

# sorted returns a sorted version of a list:
sorted(planets)

primes = [2, 3, 5, 7]
sum(primes)

# min and max to get the minimum or maximum of several arguments. 
# But we can also pass in a single list argument
max(primes)

# Interlude: objects
# In short, objects carry some things around with them. 
# You access that stuff using Python's dot syntax.
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

# A function attached to an object is called a method
# Numbers have a method called bit_length. Again, we access it using dot syntax
x.bit_length
# To actually call it, we add parentheses:
x.bit_length()

# List methods: list.append modifies a list by adding an item to the end:
# Pluto is a planet darn it!
planets.append('Pluto')

# list.pop removes and returns the last element of a list:
planets.pop()

# Searching lists: We can get its index using the list.index method.
planets.index('Earth')

# Use the in operator to determine whether a list contains a particular value:
# "Earth" in planets
# "Calbefraques" in planets

# Tuples: Tuples are almost exactly the same as lists. They differ in just two ways.
# The syntax for creating them uses parentheses instead of square brackets:
# t = (1, 2, 3)
t = 1, 2, 3 # equivalent to above
print(t)

# They cannot be modified (they are immutable).
# Cannot: t[0] = 100
# Tuples are often used for functions that have multiple return values.

#  the as_integer_ratio() method of float objects 
# returns a numerator and a denominator in the form of a tuple:
x = 0.125
print(x.as_integer_ratio())

# These multiple return values can be individually assigned as follows:
numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

# Swapping two variables!
a = 1
b = 0
a, b = b, a
print(a, b)