# Loops are a way to repeatedly execute some code
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line
# The for loop specifies
#       the variable name to use (in this case, planet)
#       the set of values to loop over (in this case, planets)

# if it can be thought of as a group of things, you can probably loop over it. 
# In addition to lists, we can iterate over the elements of a tuple:
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult  
print (product)

# Loop through each character in a string:
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')    

# range() is a function that returns a sequence of numbers
for i in range(5):
    print("Doing important work. i =", i)

# while loops: terates until some condition is met
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1

# List comprehensions: one of Python's most beloved and unique features
squares = [n**2 for n in range(10)]
print (squares)

# Do the same thing without a list comprehension
squares = []
for n in range(10):
    squares.append(n**2)
print (squares)

# We can also add an if condition:
short_planets = [planet for planet in planets if len(planet) < 6]
#   for planet in planets 
#       if len(planet) < 6
#       return planet
print (short_planets)

# filtering with an if condition and applying some transformation to the loop variable
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets
#  write these on a single line
[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

#  SELECT, FROM, and WHERE
# [32 for planet in planets]

# List comprehensions combined with functions like min, max, and sum can lead to 
# impressive one-line solutions for problems that would otherwise require several lines of code.
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
# Solution using a list comprehension
def count_negatives(nums):
    return len([num for num in nums if num < 0])
# This third solution is better still!
def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])
