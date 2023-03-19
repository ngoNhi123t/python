a =2
b=1
a+b
print(a+b)
a = "heloo how can i help you"
print(a[2:4])
print('hello /tworld')
mystring = "hello world"
print(mystring [-2])
# ddaor nguowcj ki tuwj
print(mystring[ : :-1])
print(mystring[ : : 2])
x= " hello world"
print(x+" sam")
print(x.upper())
print(x.lower())
print(x.split('o'))
# chenf vao chuoi
print('this is the string{}'.format('inter'))
print('the {} {} {}'.format('fox', 'mn', 'lm'))
print('the {1} {1} {1}'.format('fox', 'mn', 'lm'))
print('the {l} {m} {f}'.format(f ='fox',m= 'mn',l= 'lm'))
result = 200/777
print(result)
print('the result is {r:10.4f}'.format(r=result))
#{value:width.precision f}

name = "jose"
print(f'hello his name {name}')
name ="sam"
age= 3
print(f"{name} is {age}")
#list co the tha doi phan tu trong no, kha string
my_list =['a tring', 23, 100.23,'o']
print(len(my_list))
#indexing and slicing
print(my_list[0])
my_list = my_list + ['m']
print(my_list)
print(my_list*2)
# Again doubling not permanent
#them mowis
my_list.append('k')
print(my_list)
#lay phan tu cuoi vaf laays khoi list
print(my_list.pop())
print(my_list)
#lay phan tu index =1
my_list.pop(1)
print(my_list)
# sawps xep thu tuwj
new =['a','c','h','d']
num =['4','3','1','2']
new.sort()
print(new)
num.sort()
num.reverse()
print(num)
#reserse(): nguowcj laij
#DICTIONARY
#{'KEY1'='VALUE1','KEY2'}='VALUE2'...
#KHI NÀO CHỌN 1 DANH SÁCH, KHI NÀO CHỌN 1 DICTIONARY?
# DICTIONARY: có các đối tượng được truy xuất theo tên khóa(key), và từ điển không có thứ tự, không thẻ sắp xếp. Vì vậy thời điểm thích hợp sử dụng dic là khi muốn nhanh chóng truy xuất giá trị mà không cần biết vị trí chính xác của chỉ mục
my_dict={'k1':[1,2,3], 'k2':{'d':30}}
print(my_dict['k2']['d'])
d ={'k':['a','b','c']}
mylist=d['k']
print(mylist)
letter = mylist[1]
print(letter.upper())
print(letter)
print(d['k'][2].upper())
#them vào dictionary:
d['k1'] = 30
print(d)
d['k1'] = 'hello'
print(d)
print(d.keys())
print(d.values())
print(d.items())
#TUPLES :(1,2,3)
# tUPELS are very similar to lists. However they have one ley difference- IMMUTABLITY: BẤT BIẾN, KHÔNG THỂ THAY ĐỔI
# ONCE AN ELEMENT INSIDE A TUPLE, IT CAN NOT BE REASSIGNED
t = (1,2,3)
mylist =[1,2,3]
print(type(t))
print(type(mylist))
print(t[0])
print(len(t))
#đếm số 2
t=(2,2,3,4,2,5)
print(t.count(1))
# lần đầu tiên xuất hiên số 3 trong tuples
print(t.index(3))
#SETS
#sét are unordered collections of unique elements meaning there can only be one representative of the same object. 
myset = set()
myset.add(2)
print(myset)
myset.add(4)
print(myset)
# không lặp lại giá trị đã có trong đó
myset.add(2)
print(myset)
mylist = [1,1,1,1,2,2,2,3,3,3,4,4,4]
print(set(mylist))
#BOOLEANS: TRUE/ FALSE
False
print(type(False))
print(1>2)
print(1==1)
b = None
# FILES
myfile = open('laptrinhtudau.txt')
print(myfile.read())
# đọc lại từ đầu
# tìm vị trí con trỏ tại ví trí 0
myfile.seek(0)
print(myfile.read())
print(myfile.read())
# tạo 1 list mỗi phần tử là 1 dòng
myfile.seek(0)
print(myfile.readlines())
myfile.close()
my = open("D:\\hello.txt")
####
with open('D:\\hello.txt') as newfile:
    contents = newfile.read()
print(contents)
with open('D:\\hello.txt', mode='r') as hello:
    contents =hello.read()
print(contents)
# mode: r: chỉ đọc, w: chỉ viết, có thể ghi đề lên tệp và tạo tệp mới nếu chưa có 
# mode: a chỉ thêm(Add)
with open('D:\\hello.txt', mode='r') as hello:
    print(hello.read())
with open('laptrinhtudau.txt', mode='a') as hello:
    print(hello.write('\n hellooo'))
with open('laptrinhtudau.txt', mode='r') as hello:
    print(hello.read())
with open('dghskjdkjsfhj.txt', mode='w') as f:
    f.write(' I CREAT THIS FILE')
with open('dghskjdkjsfhj.txt', mode='r') as f:
    print(f.read())