n = float(input())
time = int(n/0.5)
print(" |",end="")
print("----|"*time)
for i in range(0,time+1):
    print(i*0.5,end="  ")