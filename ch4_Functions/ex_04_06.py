
def computepay(hours, rate_normal):
    if hours <= 40:
        pay = hours * rate_normal
    else:
        extra_hours = hours - 40
        hours -= extra_hours
        print(hours,extra_hours, rate_normal)
        pay = (hours * rate_normal) + (extra_hours * rate_normal * 1.5)
    return pay

input_hours = input("Enter the hours: ") 
input_rate_normal = input("Enter the rate: ")

try:
    hours = float(input_hours)
    rate_normal = float(input_rate_normal)
    pay = computepay(hours,rate_normal)
    print(pay)
except:
    print('Enter a valid number')
    quit()
