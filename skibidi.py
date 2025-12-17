t = input()


new_t = ""

for letter in t:
    if letter==" ":
        continue

    if letter.isalpha():
        new_t+= letter.upper()
    elif letter.isdigit():
        n = int(letter)
        if n%2==1:
            new_t+= str(n*3+1)
        else:
            new_t+= str(n//2)
    else:
        new_t+= letter

new_t = new_t.replace("SIGMA","ALPHA")

n = int(input())
for _ in range(n):
    print(new_t)