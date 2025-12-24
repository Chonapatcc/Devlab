lst = [int(x,16) for x in input().split()]

for letter_num in lst:
    letter = chr(letter_num)
    print(letter, end='')