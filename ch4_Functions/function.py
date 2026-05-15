#function is a named sequence of statements that performs a computation
type('This a string') #funcion name is type
                      #() expression inside is an argument -> input to the function

#Built-in 
max('Hello World') #Largest and minimun char
min('Hello World')

len('Hello World') #Lenght of char

# Type conversion
int(32)
int(3.9999) # result 3, it doesnt round up 
float(3.14)
str(42) 

import math
#print(math) #Module object named math
# access the functions within the module use math.function()
signal_power = 10
noise_power = 1
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)

degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)
0.7071067811865476

#Random
import random
#Pseudorandom because are created by deterministic computation -> predictable results always.  
#Number between 0.0 and 1.0, including 0.0 but not 1.0
for i in range(10):
    x = random.random()
    #print(x)


# Range (low,high)
random.randint(5,10)

# Between a sequence 
t = [1,2,3]
random.choice(t)

# Random values from continuous distributions including Gaussian, exponential, gamma, etc.

#Defining, storing the function 
#               () -> doesnt take any arguments as input 
def print_lyrics():         # Header of the function: 
    print("Holaaa")             # Body: first statement
    print("Holaaa")             # Body of the function all indented 
    print("Holaaa 2")           # Body 

# Creates a variable named print_lyrics and is type function
#Invokes or calls
#print_lyrics()

# Use inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    

#repeat_lyrics()

#Function definition creates a function object, and generates no output
# 
#Flow of execution
#order in which statements are executed
# When reading a program: makes more sense if you follow the flow of execution

# Parameters and arguments
#Inside the function the arguments are assigned to variables called Parameters
#This function assigns the argument(when calling the function) to a parameter named bruce (defined when using def function_name(parameter))
#When the function is called, it prints the value of the parameter

def print_twice(bruce): # Parameter -> bruce
    print(bruce)
    print(bruce)

#print_twice("Sam "*4)   # Argument ->  "Sam "*4

# Fruitful functions and void functions

#  yield results    | |  don’t return a value
#fruitful function: 
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2         # In the interactive mode in the terminal using python, this is prompted but in a script it needs a print
#print(golden)

# Void functions dont return a value.
# When you try to assign it to a variable it displays a special value: None

#result = print_twice('Hola')
#print(result)
#print(type(result))     # Special class type called None

# Fruitful function return a result from the function 
def add_two(a,b):       # Parameters: a, b
    added = a + b
    return added

x = add_two(1,2)        # Arguments: 1, 2
print(x)
print(type(x))     # Class type int

# Why functions? 
#   - Name and group a set of statements, program is easier to read, understand and debug
#   - Eliminate repetive code. Reuse code.
#   - Dividing a long program into functions allows to debug the fraction parts one at a time, then integrating all as a whole.
#   - Well-design functions are often useful for many programs. 