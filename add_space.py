string = input()
isPrintedFirst = False
for i in string:
    if i.isupper():
        if isPrintedFirst:
            print(' ', end='')
        print(i, end='')
        isPrintedFirst = True
    else:
        print(i, end='')