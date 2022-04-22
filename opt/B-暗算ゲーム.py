s = input()
x = 0

for i in range(len(s)):
    if i % 2 == 0:
        x += int(s[i])
    else:
        x -= int(s[i])

print(x)

