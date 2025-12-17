n = int(input())
arr = [int(input()) for _ in range(n)]

count =0 
for i in range(n):
    if arr[i] == -1:
        continue
    for j in range(i+1,n):
        if arr[j] == -1:
            continue
        if arr[i] == arr[j]:
            count += 1
            arr[i] = -1
            arr[j] = -1
            break
print(count)
