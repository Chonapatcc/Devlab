t = input()

count = 0
for i in range(len(t)):
    if t[i]=='X':
        continue
    if i==0 : 
        if t[i+1]=='O':
            count+=1
        continue
    if i==len(t)-1 :
        if t[i-1]!='X':
            count+=1
        continue
    if t[i-1]=='O' and t[i+1]=='O':
        count+=1
print(count)
