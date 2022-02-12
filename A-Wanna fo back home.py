S = input()
n = 0
w = 0
s = 0
e = 0
x = len(S)
for i in range(x):
    if S[i] == 'N':
        n += 1
    elif S[i] == 'W':
        w += 1
    elif S[i] == 'S':
        s += 1
    elif S[i] == 'E':
        e += 1

if n == 0 and s == 0:
    if e * w != 0:
        print('Yes')
    else:
        print('No')

elif n != 0 and s != 0:
    if e * w != 0:
        print('Yes')
    elif e == 0 and w == 0:
        print('Yes')
    else:
        print('No')

else:
    print('No')

