n = int(input())

prime_list = []

for i in range(2,n):
    is_prime = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)

if len(prime_list) == 0:
    print('None')
else:
    print(prime_list[-1])