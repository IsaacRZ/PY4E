# Defined loops run defined number of times.
# Run finite number of times. iterates through the members of a list, set

#for i in [5,4,3,2,1]:
#    print(i)
#print('BlastOff!')

#friends = ['Jose','Glenn', 'Sally']
#for friend in friends:
#    print('Happy New Year',friend)
#print('Done!')

# Have explicit iteration variables, changes each time trough a loop.
# These iteration variables move through the sequence = ordered set.

# Loop Idioms:
#Basic loop
#print('Before')
#for thing in [9,41,13,3,67,5]:
#    print(' ',thing)
#print('After')

#largest_so_far = -1 
#print('Before',largest_so_far)
#for i in [9, 41, 12, 3, 74, 15]:
#    if i > largest_so_far:
#        largest_so_far = i
#    print(largest_so_far, i)
#print('After',largest_so_far)

# Counting in a loop
#zork = 0            # Count mnemonic
#print('Before',zork)
#for thing in [9, 41, 12, 3, 74, 15]:
#    zork = zork + 1
#    print(zork, thing)
#print('After',zork)

#zork = 0            # Count mnemonic
#print('Before',zork)
#for thing in [9, 41, 12, 3, 74, 15]:
#    zork = zork + thing
#    print(zork, thing)
#print('After',zork)

#sum = 0
#count = 0
#for i in [9, 41, 12, 3, 74, 15]: # iterative variable
#    count = count + 1
#    sum = sum + i
#    print(count, i, sum)
#count = 0


#for i in [9, 41, 12, 3, 74, 15]: # iterative variable
#    if i > 20:
#        print( i, 'Número mayor a x')

#found_value = False
#print(found_value, 'Valor al iniciar')

#for i in [9, 41, 12, 3, 74, 15]: # iterative variable
#    if i == 3:
#        found_value = True
#        print( i, 'Número coincide:',found_value)
#    else:
#        found_value = False
#        print( i, 'Número NO coincide:',found_value)

#smallest1
#smallest = None
#count = 0 
#for i in [9, 41, 12, 3, 74, 15]: # iterative variable
#    count += 1 
#    if smallest == None:
#        smallest = i
#        print( count,i, 'El número menor es:',smallest)
#    elif smallest < i:
#        print( count,i, 'El número menor es:',smallest)
#smallest2
#smallest = None
#count = 0 
#for i in [9, 41, 12, 3, 74, 15]: # iterative variable
#    count += 1 
#    if smallest == None or i < smallest:
#        smallest = i
#        print( count,i, 'El número menor es:',smallest)
#    else:
#        print( count,i, 'El número menor es:',smallest)
#print("Done")

#is and is not operator
# stronger than == !=
# it ask if is (or is not) equal two objects in type and value
#print(0 == 0.0)     # T         No conversion of data type
#print(0 is 0.0)     # F
# use it on Booleans and None types
# dont use on int, float nor strings


