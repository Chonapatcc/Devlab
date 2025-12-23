t = input()

dic = {}
for i in t:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

odd_count = 0
for count in dic.values():
    if count % 2 != 0:
        odd_count += 1
print(odd_count <= 1)