s = 'Monty Python'
#print(s[0:4]) # Read s, subzero([]) through(:) four but not including four
#print(s[6:7]) # Read s, 6 through  7 but not including 7
#print(s[6:40]) # Read s, 6 through  40
#print(s[:2])    #  [:3] from beginning
#print(s[8:])    #  [3:] from end
#print(s[:])    #  [:] All

#Concatenation
#a = 'Hello'
#b = 'There'
#print(a +' '+ b)
#print(a , b)

# In: logical op
fruit = 'banana'
#print('n' in fruit)
#print('nan' in fruit)
#if 'a' in fruit:
#    print('Found it!')

#Compare character set of the computer and Character set python is
# Lexographically less than or greater than
word = fruit
#if word == 'banana':
#    print('Al right!')

#if word < 'banana':
#    print('Al right is less than!')
#elif word > 'banana':
#    print('Al right word is greater than!')

import string
# Method call .method() -> object oriented special function
word_upper = word.upper()   # word is still the same
word_lower = word.lower()   # method gives back a lower case copy of the original object without changing it 
#print(word_upper,word_lower)
#print(dir(word))            # Methods available to do on strings 

position_fruit = fruit.find('a')
#print(position_fruit)
replace_fruit = fruit.replace('a','x')
#print(replace_fruit)

#Clean white spaces 
greet = '   Hello    There    '
greet_lower = (greet.strip())
#print(greet.lstrip())
#print(greet.rstrip())
#print(greet.strip())
#print(greet_lower.startswith('H'))

data = 'From isaac@cuc.ac.cr Sun May 13:24:50 2026'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)