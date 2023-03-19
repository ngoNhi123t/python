name = input('Enter s file name:')
try:
   handle = open(name) 
   #open, close, read, write
except:
    print('File cannot be')
    exit()
# inp = handle.read()
# fino = inp.upper()
# print(fino)
# count =0
# for line in handle:
#      count= count +1
# print(count)
# for line in inp:
#     lin = line.upper()
#     print(lin)
for line in handle:
    if line.startswith('>>>'):
        print(line)