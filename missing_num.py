t = input().split(" .. = ")
num1, num2 = t[0], int(t[1])
num1,op = num1.split(" ")
num1= int(num1)
result = 0
if op == "+":
    result = num2 - num1
elif op == "-":
    result = (num2 - num1)*-1
elif op == "*":
    result = num2 // num1
elif op == "/":
    result = num1 // num2

if result==0:
    print("Error")
else:
    if op =="*":
        op = "x"
    print(f"{num1} {op} {result} = {num2}")

