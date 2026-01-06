t = input()

stack = []
left = "({["
right = ")}]"
valid = True
for char in t:
    
    if char in left:
        stack.append(char)
    elif char in right:
        if len(stack) == 0:
            valid = False
            break
        top = stack.pop()
        if (top == '(' and char == ')') or (top == '{' and char == '}') or (top == '[' and char == ']'):
            continue
        else:
            valid = False
            break

if valid:
    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

# print(stack)