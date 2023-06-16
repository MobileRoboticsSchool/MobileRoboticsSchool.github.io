# Here are a few examples of function declarations (definition)
# printHelloWorld: no arguments, no output
def printHelloWorld():
  print("Hello world")

# div: input = 2 integers; output = 1 float
def div(a,b):
  return a/b

# splitStringAtComma: input = 1 string; output = list of strings
def splitStringAtComma(s):
  return s.split(",")

# fibonacci: input = 1 iinteger; output = 1 integer
def fibonacci(n):
  x_nm1 = 0
  x_nm2 = 1
  for i in range(n):
    x_n = x_nm1 + x_nm2
    x_nm2 = x_nm1
    x_nm1 = x_n
  return x_nm1

# those were only the definitions of the functions. Now that 
# they are defined we can use them as such:
printHelloWorld()
f = div(1,4)
l = splitStringAtComma("str1,str2")
r = fibonacci(10)

print(f)
print(l)
print(r)

