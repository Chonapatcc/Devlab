import math
def combination(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

a,b = map(int, input().split())
result = combination(a, b)
print(result)