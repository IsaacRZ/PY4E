count = 0
total = 0
while True:
    svar = input('Enter a number: ')
    if svar == 'done':
        break
    try:
        fvar = float(svar)
    except:
        print('Invalid input')
        continue
    count += 1
    total += fvar
    print(count, fvar, total)

print('Avg:',total /count,'Total:',total)
    
