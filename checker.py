data = [int(x) for x in input()[1:-1].split(',')]
validater = [int(x) for x in input()[1:-1].split(',')]

score =0 
for i in range(len(data)):
    if data[i] != validater[i]:
        if data[i] ==0:
            score -=3
        else:
            score -=1
    else:
        score +=3

print(max(score,0))