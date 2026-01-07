def calculate_fare(age, distance, type_bus):
    if age>=60:
        return 0
    
    fare = 0
    if type_bus==0:
        if distance<=15:
            fare = 8
        elif  distance<=30:
            fare = 16
        else:
            fare =24
    elif type_bus==1:
        if distance<=15:
            fare = 15
        elif  distance<=30:
            fare = 30
        else:
            fare =35
    if age<=15:
        fare -=5
    elif age>=50:
        fare -=2
    return fare 


age = int(input())
distance = int(input())
type_bus = int(input())

fare = calculate_fare(age, distance, type_bus)
if fare==0:
    print("FREE")
else:
    print(fare,"Bath")
