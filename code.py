import re 

file1 = open("book1.txt", "r", encoding="utf8")
file2 = open("book2.txt", "r", encoding="utf8")

list1 = file1.read()
list2 = file2.read()
list1 = re.findall(r"[\w']+", list1)
list2 = re.findall(r"[\w']+", list2)

common_words=set()

for i in list1:
    if i.lower() in common_words:
        continue
    for j in list2:
        if i.lower() == j.lower():
            common_words.add(i.lower())

for i in common_words:
    print(i+" ")

print("\nThe number of common words is",len(common_words))