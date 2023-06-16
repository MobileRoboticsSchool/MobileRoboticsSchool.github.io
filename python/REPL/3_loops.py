# Imagine I want to increment a variable x from 0 to 5 
# and show it's value changing. I could write:
print("No loop")
x = 0
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)

# But that is highly unreadable and unpractical. 
# Therefore python and most other programming langage use 
# loops. In python we'll use the for loop:

print("\nFor loop")
x = 0
for i in range(5):
  x = x + 1
  print("x = ", x)

# Note that the two previous bits of code give the same output. 
# At first it can be fine to understand "for i in range(5):..." 
# as "repeat 5 times...", although it means a bit more than that.

# Another thing to notice here is the use of indentations in python: 
#the lines 21 and 22 start with a tabulation, it means that the two 
# form a block, and this whole block will be repeated by the for 
# loop in line 20.

# Repetitions can also be handled by While loops. Which leads us 
# to a third way to do the same thing: 
print("\nWhile loop")
x = 0
while x < 5:
  x = x + 1
  print("x = ", x)
