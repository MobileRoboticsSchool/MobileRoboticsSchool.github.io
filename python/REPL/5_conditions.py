# fibonacci: input = 1 iinteger; output = 1 integer
def fibonacci(n):
  x_nm1 = 0
  x_nm2 = 1
  for i in range(n):
    x_n = x_nm1 + x_nm2
    x_nm2 = x_nm1
    x_nm1 = x_n
  return x_nm1

# I'll take this opportunity to show you one more little 
# instruction: input. When you use input, the user is asked 
# to type something in the terminal which is returned to the 
# program,  allowing to make the code interactive.

while True:
  s = input('Which Fibonacci number do you want? ')
  # as input returns a string and we want a number
  # we convert if to integer
  n = int(s)
  # print the result
  print("Fibonacci(",n,") = ",fibonacci(n),"\n")

# Try it out and try to understand what is going on. One problem 
# you will find (especially if you try to make things crash as I 
# asked you to do) is that if someone types something like "not 
# a number" as an input, the code will crash. Indeed the function 
# int() does not accept to convert non digits. 
# To prevent this we can use a condition and check if our string 
# is made of digits such as:

if s.isdigit():# s.isdigit() returns either True or False
  print("s is a positive nunmber")
  # dosomethingmore
else:
  print("s is not a positive nunmber")
  # dosomethingmore

# (Note that this piece of code will never be executed because 
# if comes after a While True: loop)
# Try to add such a condition inside the while loop to remind 
# the user to put numbers if he's not doing so.