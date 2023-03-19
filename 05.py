

tong = 0
while True:
    a = input('enter a number:')
    if a == 'done':
        break
    try:
       c = float(a)
    except:
        print('invalid input!')
    print (c)
    tong = tong + c
print(tong)
    
    
    
