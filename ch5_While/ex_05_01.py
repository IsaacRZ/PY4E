#count = 0
#total = 0.0
#
#while True:
#    sval = input('Enter a number: ')
#    if sval == 'done':
#        break
#    try:
#        fval = float(sval)
#    except:
#        print('Invalid input')
#        continue
#    
#    count += 1
#    total += fval
#    print(count, fval,'total: ',total)
#print('average', total/count,'total: ',total)

count = 0
total = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    
    count += 1
    total += fval
    print(count, fval,'total: ',total)
print('average', total/count,'total: ',total)