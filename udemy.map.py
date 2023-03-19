#map(func, interiable)
def square(num):
    return num**2
my_nums=[1,2,3,4,5,6]
for item in map(square, my_nums):
    print(item)
print(list(map(square, my_nums)))
def check_even(num):
    return num %2==0
mynums=[1,2,3,4,5,6]
print(list(filter(check_even, mynums)))
# def square(num):
#     return num**2
#chỉ sd 1 lần: lambda

square = lambda num: num**2
square(10)
print(list(map(lambda num:num**2, my_nums)))
names=['sany','petter']
print(list(map(lambda x: x[::-1],names)))

### Nested
###LEGB Rule:

#L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

#E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

#G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

#B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

#local
# lambda num: num**2
#enclosing function local
#GLOBAL
name=' THIS IS A GLOBAL STRING'

def greet():
    #ENCLOSING
    name='sammy'
    
    def hello():
        #LOCAL
        name="I AM A LOCAL"
        print('hello '+name)
    hello()
greet()

###
x=50
def func(x):
    # global x
    print(f'x is {x}')
    #LOCAL REASSIGNMENT , now on a global variable
    x= 'NEW VALUE'
    print(f'i just locally changed X to {x}')
    return x
# print(x)
func(x)
print(x)
## HOMEWORK
import math
def vol(rad):
    pi= math.pi
    # print(pi)
    v = (4/3)*pi*pow(rad,3)
    return v
# Check
print(vol(2))

#02
def ran_check(num,low,high):
    if num >=low and num<= high:
        print(f"{num} is in the range between {low} and {high}") 
    else:
         print(f"{num} is not in the range between {low} and {high}") 
    pass
# Check
ran_check(8,2,7)

#cach 2:
def ran_bool(num,low,high):
     if num >=low and num<= high:
         return True
     else:
         return False
    
print(ran_bool(3,1,10))
# nam ='nam nMK'
# print(nam[5].isupper())
def up_low(s):
    
    x = len(s)-1
    lows = 0
    hights =0
    add = True
    for i in range(x):
        while add:
            if s[i].isupper()== True:
                hights+=1   
                break        
            else:
               add = False              
        while not add:
            if s[i].islower()== True:
                lows +=1
                break
            else:
                 add =True
                 break
    print(f"No. of Upper case characters : {hights}")
    print(f"No. of Lower case Characters : {lows}")    
    pass
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)
