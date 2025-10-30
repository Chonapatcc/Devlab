
card  = input()

s= 0 
for i in range(0,12):
    s+= int(card[i])*(13-i)

s= (11- s%11)%10
if s == int(card[12]):
    print("Pass")
else:
    print("Fail")
