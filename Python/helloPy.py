# Create a variable called spam_amount and assign it the value of 0 using =
spam_amount = 0

print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0: # The colon (:) at the end of the if line indicates that a new code block is starting. 
    print("But I don't want ANY spam!") # Subsequent lines which are indented are part of that code block.

# Multiply a string by a number, to get a version that's been repeated that many times
viking_song = "Spam " * spam_amount
# Spam x 4 = Spam Spam Spam Spam

print(viking_song)

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

print(6 / 2) # It always gives us a float.

# The // operator gives us a result that's rounded down to the next integer.
print(5 // 2)

# min and max return the minimum and maximum of their arguments, respectively...
print(min(1, 2, 3))
print(max(1, 2, 3))

# abs returns the absolute value of an argument:
print(abs(32))
print(abs(-32))

#int and float can also be called as functions which convert their arguments to the corresponding type
print(float(10))
print(int(3.33))

# They can even be called on strings!
print(int('807') + 1)

