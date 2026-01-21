prime_list = []
def is_prime(n):
    if n == 2 or n ==3 :
        return True
    half = int(n**0.5)+1
    for num in prime_list:
        if num > half:
            break
        if n % num == 0:
            return False
    return True


n = int(input())
for i in range(2, n + 1):
    if is_prime(i):
        prime_list.append(i)
print(prime_list[-1])