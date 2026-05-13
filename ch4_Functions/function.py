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
print(math) #Module object named math
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
#Pseudorandom because are created by deterministic computation. 
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

# Creates a variable named print_lyrics and is type function
#Invokes or calls
#print_lyrics()

# Use inside another function
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():         # Header: 
    print("Holaaa")             # Body first statement
    print("Holaaa")             # Body  all indented 
    print("Holaaa 2")           # Body

repeat_lyrics()

#Function definition creates a function object 