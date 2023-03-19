#1
# hours = input('Enter hours:')
# rates = input('Enter rates:')
# if float(hours) <= 40.0:
#     pay = float(hours)*float(rates)
# else:
#     pay = 40.0 * float(rates)+ (float(hours)-40.0)*float(rates)*1.5
# print('Pay:', pay)
#2
# hours = input('Enter hours:')
# try:
#     hr = float(hours)
# except:
#     print('Error, please enter numeric input')
# rates = input('Enter rates:')
# try:
#     rt = float(rates)
# except:
#     print('Error, please enter numeric input')
# if float(hr) <= 40.0:
#     pay = float(hr)*float(rt)
# else:
#     pay = 40.0 * float(rt)+ (float(hr)-40.0)*float(rt)*1.5
# print('Pay:', pay)
#3
diemso = input('Enter score:')
try:
    diem = float(diemso)
except:
    print('Please enter numberic!')
if diem >= 0.0 and diem <= 1.0:
    if diem >= 0.9:
        print('A')
    elif diem >= 0.8:
        print('B')
    elif diem >= 0.7:
        print('C')
    elif diem >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('bad score')
    
