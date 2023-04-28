# Tao duong dan File
duong_dan = "D:\laptrinhtudau.txt"
# Che do doc file
che_do = "r"
# Ham open de mo file
f = open(duong_dan,che_do)
# Duyet qua File
for each in f:
    print(each,end=" ") # Hien thi tung tu co trong File