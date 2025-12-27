def print_star(n,x):
    print(" "*(x-n) + "*"* (2*n -1))
n = int(input())


for i in range(0,n):
    print_star(n-i,n)