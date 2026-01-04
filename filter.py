def print_list(list,type):
    if len(list)==0:
        return
    print(f"{type}(s):")
    for item in list:
        if item==' ':
            continue
        print(item,end=' ')
    print()

text =input()
vowels = "aeiouAEIOU"
numbers = "0123456789"

vowels_list = []
numbers_list = []
consonants_list = []

for char in text:
    if char in vowels:
        vowels_list.append(char)
    elif char in numbers:
        numbers_list.append(char)
    else:
        consonants_list.append(char)

print_list(vowels_list,"Vowel")
print_list(consonants_list,"Alphabet")
print_list(numbers_list,"Number")