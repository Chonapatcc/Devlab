def print_num(num,left_padding):
    digits = {
        '0': [
            " -- ",
            "|  |",
            "|  |",
            "|  |",
            " -- "
        ],
        '1': [
            "    ",
            "   |",
            "   |",
            "   |",
            "    "
        ],
        '2': [
            " -- ",
            "   |",
            " -- ",
            "|   ",
            " -- "
        ],
        '3': [
            " -- ",
            "   |",
            " -- ",
            "   |",
            " -- "
        ],
        '4': [
            "    ",
            "|  |",
            " -- ",
            "   |",
            "    "
        ],
        '5': [
            " -- ",
            "|   ",
            " -- ",
            "   |",
            " -- "
        ],
        '6': [
            " -- ",
            "|   ",
            " -- ",
            "|  |",
            " -- "
        ],
        '7': [
            " -- ",
            "   |",
            "    ",
            "   |",
            "    "
        ],
        '8': [
            " -- ",
            "|  |",
            " -- ",
            "|  |",
            " -- "
        ],
        '9': [
            " -- ",
            "|  |",
            " -- ",
            "   |",
            " -- "
        ]
        ,
        'blank': [
            "    ",
            "    ",
            "    ",
            "    ",
            "    "
        ]
    }
    for i in range(5):
        line = ' ' * left_padding*5
        for digit in str(num):
            line += digits[digit][i] + ' '
        print(line)
    return
 
num1 = int(input())
num2 = int(input())
result = num1 + num2

size = len(str(result))

print_num(num1, size - len(str(num1)))
print_num(num2, size - len(str(num2)))

print("-"*(size*5 - 1))
print_num(result, 0)
print("="*(size*5 - 1))