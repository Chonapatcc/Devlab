temp = input()
if ',' in temp:
    lst = [int(x) for x in temp.split(',')]
else:
    lst = [int(x) for x in temp.split(' ')]
want = int(input())
found = False
for i in range(len(lst)):
    if lst[i] >= want:
        continue
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == want:
            print(f"[{i},{j}]")
            exit()
        if lst[i] + lst[j] > want:
            break
print(0)
