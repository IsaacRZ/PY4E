# Convert data types fromt user prompt input
#inp = input('Enter Farenheit Temperature:\n')
#try:
#    fahr = float(inp)
#    cel = (fahr - 32) * 5/9
#    print(cel)
#except:
#    print('Enter a valid number')

#Catching an exception 

#Short Circuiting eval
#Eval of a logical expressions stops because the overall result is already known 
#Stops the evaluation and doesnt do the computations on the rest of the logical expression 
#GUARDIAN PATTERN
#x = 1
#y = 0
#print(x >= 2 and (x/y) > 2)
#
#x = 4
#y = 0
#print(x >= 2 and (x/y) > 2)

# GUARD EVAL
# Construct logical exp -> strategically place a guard before the evaluation might cause error

#x = 8
#y = 0
#print(x >= 2 and y != 0 and (x/y) > 2)

# Debugging
# Useful parts:
#   - Kind of error
#   - Where it occured

#error messages indicate where the problem was discovered 
# but the actual error might be earlier in the code, sometimes on a previous line

#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
hours = 45
rate_normal = 10

if hours <= 40:
    pay = hours * rate_normal
else:
    extra_hours = hours - 40
    hours -= extra_hours
    print(hours, extra_hours)
    pay = (hours * rate_normal) + (extra_hours * rate_normal * 1.5)
print(pay)

