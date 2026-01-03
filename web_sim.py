header =input()=='true'
n = int(input())
footer = input()=='true'

head = "| HEADER |"
body = "|  BODY  |"
line = "----------"
foot = "| FOOTER |"
if header:
    print(line)
    print(head)

for i in range(n):
    print(line)
    print(body)

print(line)


if footer:
    print(foot)
    print(line)