n = int(input())
lst = [int(x) for x in input().split()]
lst.sort()
print(lst[-1],lst[0])