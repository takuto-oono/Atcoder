S = input()
x = 0
for i in range(len(S)):
    if S.count(S[i]) == 2:
        x += 1

if x == 4:
    print('Yes')
else:
    print('No')