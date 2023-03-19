# def computepay(a,b):
#     pay=0
#     if float(a)<= 40.0:
#         pay= float(a)*float(b)
#     else:
#         pay= 40*float(b) + (float(a)-40)*1.5*float(b)
#     print('Pay:',pay)
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
# computepay(hr,rt)
#7
def computegrade(a):
    if a >= 0.0 and a <= 1.0:
     if a>= 0.9:
        print('A')
     elif a >= 0.8:
        print('B')
     elif a >= 0.7:
        print('C')
     elif a >= 0.6:
        print('D')
     else:
        print('F')
    else:
      print('bad score')
diemso = input('Enter score:')
try:
    diem = float(diemso)
except:
    print('Please enter numberic!')
computegrade(diem)


