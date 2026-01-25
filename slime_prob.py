cage_num, slime_size = map(int, input().split())

arr = [0]*(cage_num+1)

arr[0] = 1

for i in range(1, cage_num+1):
    val1 = arr[i-1]
    val2 = 0 
    if i - slime_size >= 0:
        val2 = arr[i - slime_size]
    arr[i] = (val1 + val2) % 1000000007

print(arr[cage_num])
