number, text = input().split()
number = int(number)

lst = "FBRS"
check = True

if number <0 or number >99:
    print("Sorry we not found that Table number :(")
    check = False
if check:
    for l in text:
        if l not in lst:
            print(f"Sorry we do not have {l} in our menu")
            check = False
            break

if check:
    print(f"Table {number} order {text}, Please Wait your order from chef :)")

    