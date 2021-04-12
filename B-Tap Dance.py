s = input()
x = 0


for i in range(1,len(s),2):
    if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
        x += 1

for i in range(0,len(s),2):
    if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
        x += 1


if x == len(s):
    print('Yes')
else:
    print('No')