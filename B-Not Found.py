S = input()
list = [chr(i) for i in range(97, 97 + 26)]
x = 0
for i in range(26):
    if list[i] in S:
        x += 1
if x == 26:
    print('None')
    exit()
for i in range(26):
    if list[i] not in S:
        print(list[i])
        exit()