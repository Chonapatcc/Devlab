text = input()

texts = []

temp = ""
for letter in text:
    if letter.isdigit():
        temp += letter
    else:
        if temp:
            texts.append(int(temp))
            temp = ""
        texts.append(letter)
if temp:
    texts.append(int(temp))

for i in range(len(texts)):
    item = texts[i]
    if item == '*':
        texts[i-1] = texts[i-1] * texts[i+1]
        texts[i] = ''
        texts[i+1] = ''
    elif item == '/':
        texts[i-1] = texts[i-1] // texts[i+1]
        texts[i] = ''
        texts[i+1] = ''
texts = [x for x in texts if x != '']
for i in range(len(texts)):
    item = texts[i]
    if item == '+':
        texts[i-1] = texts[i-1] + texts[i+1]
        texts[i] = ''
        texts[i+1] = ''
    elif item == '-':
        texts[i-1] = texts[i-1] - texts[i+1]
        texts[i] = ''
        texts[i+1] = ''
texts = [x for x in texts if x != '']
print(texts[0])




