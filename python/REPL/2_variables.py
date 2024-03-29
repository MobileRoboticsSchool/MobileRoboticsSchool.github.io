# A variable has a name. Lets call it x like you probably 
# often do in mathematics. To give x a value, it's simple, 
# just make it equal to something:

print("Assignement")
x = 0

# Now let's check what's inside x with the print function 
# that we used in the previous section:

print("x =")
print(x)

# actually let's make this a bit more tidy and enjoy the 
# capability of print to take several arguments

print("x = ",x)

# There exist different types of variables. During the 
# summerschool we'll use mostly integers (numbers), 
# floats(decimal numbers), strings (text), booleans (True of False) 
# and lists (lists...)

print("\nTypes")# \n = end of line
myInt = 2020
myFloat = 3.14
myString = "Hello world"
myBoolean = True
myList = ["Kate","Joe", "Ben", "Shanka"]

print(myInt)
print(myFloat)
print(myString)
print(myBoolean)
print(myList)

# Each type comes with it's operations. As you could expect if 
# I add two numbers and if I add two strings, the process will be very different. Let's try it out:

print("\nOperations")
print(myInt + 1)
print(myFloat / 2)
print(myString + " !!!")
print(not(myBoolean))
print(myList[3])

# Note that you can use the value stored in a variable to 
# assign another variable. And then you can end up with things 
# a bit strange at first but super useful such as this:

print("\nOperations2")
print(x)
x = x + 1
print(x)

# One last thing. Can we add strings and integers ? 
# What do you think ?

print("\nOperations3")
myString = "Year:" + 2000
print("myString")

# This does not work and that is great ! 
# Indeed adding a string and an integer is ambiguou. 
# What do we want out of that is unclear. 
# Do we want 2000 to be converted to a string and concatenated 
# to "Year", or do we want "Year" to be converted in ascii and 
# added to 2000. The computer is not supposed to know and does 
# not take the decision for us which is great. Instead he gives 
# an error where it explains us why he has a problem with what we 
# wrote. Pay attention to those errors and try to understand them, 
# that's the best way to become independant and open yourself the 
# world of computer science (and a big part of robotics).

