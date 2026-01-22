from math import gcd

def cross(key1, key2):
    map = {}
    for i in range(2):
        for j in range(2):
            key = key1[i] + key2[j]
            
            if key[0] > key[1]:
                key = key[::-1]
            
            if key in map:
                map[key] += 1
            else:
                map[key] = 1

    return map

def get_value(key1,key2,key3):
    map = cross(key1,key2)
    return map[key3] if key3 in map else 0



n =  int(input())
for _ in range(n):
    a,b,c = input().split()
    size = len(a)//2
    not_exist = False
    top_list = []
    for i in range(size):
        key1 = a[i*2:(i+1)*2]
        key2 = b[i*2:(i+1)*2]
        key3 = c[i*2:(i+1)*2]
        value = get_value(key1,key2,key3)
        if value == 0:
            not_exist = True
            break
        else:
            top_list.append(value)
            
    if not_exist:
        print("0")
        continue
    
    down = pow(4,len(top_list))
    top = 1
    for val in top_list:
        top*=val

    if top == down:
        print("1")
        continue

    g = gcd(top,down)
    print(f"{top//g}/{down//g}")
        
        
    