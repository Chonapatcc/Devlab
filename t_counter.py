t=input()
c=0
for i in t:
    if i.isdigit() or i.isalpha():
        c+=1
print(c)