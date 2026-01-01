def tower_of_hanoi(n, source, target, auxiliary):

    if n == 1:
        print(f"{source}{target}",end=" ")

        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"{source}{target}",end=" ")

    tower_of_hanoi(n - 1, auxiliary, target, source)

n = int(input())

tower_of_hanoi(n, 'A', 'C', 'B')

