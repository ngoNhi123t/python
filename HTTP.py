# import urllib.request

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
# coi là 1 tệp đọc qua vòng lặp for với urllib.urlopen 
    
#2
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://books.trinket.io/pfe/12-network.html')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)