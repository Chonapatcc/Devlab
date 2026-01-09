lst = input().split()
size = len(lst)
for i in range(size):
    if lst[i]=="?":
        if i+2 <size:
            a = int(lst[i+1])
            b = int(lst[i+2])
            print(a - (b-a) )
        elif i-2 >=0:
            a = int(lst[i-1])
            b = int(lst[i-2])
            print(a + (a-b))
        break