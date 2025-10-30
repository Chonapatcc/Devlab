lst = [2,3,5]
a,b = int(input()),int(input())


for i in range(4,b+1):
  for j in lst:
    if i % j == 0:
      break
  else:
    lst.append(i)
for k in lst:
  if a <= k <= b:
    print(k,end=' ')