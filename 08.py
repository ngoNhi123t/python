num = [10, 60, 30, 40]
num.sort()
print(num)
letter = ['crunchy frog', 'ram bladder', 'lark vomit']
for i in range(len(num)):
    num[i] = num[i]*2
print(num)

c=num + letter
print(c)

c = num *2
print(c)

c = num[2:]
print(c)
num[1:3] = ['x', 'y']
print(num)

num.append('z')
print(num)
num.extend (letter)
print(num)

m = num.pop(0)
print(num)
print(m)
# del num[0]
# num.remove('20')
