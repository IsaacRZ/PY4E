#Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by
#printing a message and exiting the program. The following shows two executions of the program:
#
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

hours = input("Enter the hours: ") 
rate_normal = input("Enter the rate: ")
try:
    hours = float(hours)
    rate_normal = float(rate_normal)
except:
    print('Enter a valid number')
    quit()

if hours <= 40:
    pay = hours * rate_normal
else:
    extra_hours = hours - 40
    hours -= extra_hours
    print(hours, extra_hours)
    pay = (hours * rate_normal) + (extra_hours * rate_normal * 1.5)
print(pay)