t = input()

mapping = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

text = ""
for i in range(len(t)):
    if t[i].isdigit():
        if i>0 and t[i-1].isdigit():
            text+=" "+mapping[t[i]]
        else:
            text+=mapping[t[i]]
    else:
        text+=t[i]

print(text.strip())