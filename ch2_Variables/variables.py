#Values
#1,2,"Hello World"

#Types
print(type(3))
print(type(3.14))
print(type("Hola"))

#Semantic errors
#Code runs but doesn't do what expected
x = 1 , 2 , 3
print(x)
print(1,00000,00000)

#Variables
message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931
print(message, n, pi)

# Contains: numbers, letters and underscores
# 123variable -> not valid, start with number
# variable123 -> valid
# ___variable -> writting code for libraries

# class -> Reserved words:
#
# False      await      else       import     pass
#None       break      except     in         raise
#True       class      finally    is         return
#and        continue   for        lambda     try
#as         def        from       nonlocal   while
#assert     del        global     not        with
#async      elif       if         or         yield

#STATEMENTS
# Unit of code Py Interpreter can execute: Expression statement and assignment
# 
# Expression statement
print("Hola")
#Produces an output 
# 
# Assignment statement
y = 1
#Produces NO output (if is not an interactive mode)

# Operators and operands
# +, -, *, /, and **
hour=60
minute=60
20+32
hour-1
hour*60+minute
minute/60 # The result is a floating point result 
minute//60 # Obtain the same result in Python2, to floor the result
5**2
(5+9)*(15-7)

#Expressions
# combination of values, variables, and operators
# Interactive mode: the interpreter throws a result but not in an script file.

#ORDER OF OPERATIONS: PEMDAS from Left to Right 
#Parenthesis
#Exponent
#Multiplication
#Division
#Addition
#Substraction
#   2 * (3-1) = 4 
#   (1+1)**(5-2) = 8

#MODULUS Op: %
# yields the remainder 
#  check whether one number is divisible by another: if x % y is zero, then x is divisible by y
#  extract the right-most digit or digits from a number. x % 10 yields the right-most digit of x (in base 10). Similarly, x % 100

#String Operations
print('first' + 'second')
print('1' + '2')
print('first' * 3)

#Asking for input
inp = input("Ingrese numero: ") #Always saves a string
integer_inp = int(inp)          # Convert it to int
integer_inp = float(inp)        # Convert it to float

name = input('What is your name?\n')
print("Hello",name)

#mnemonic variable names: mnemonic means “memory aid”
#avoid reserved words
#chose variable names that reflect their intent regarding what data will be stored in each variable


