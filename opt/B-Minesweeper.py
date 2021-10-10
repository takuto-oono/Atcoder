h, w = map(int,input().split())
S = []
for i in range(h):
    s = input()
    s = list(s)
    S.append(s)

for i in range(h):
    for j in range(w):
        if S[i][j] == '.':
            S[i][j] = 0

for i in range(h - 1):
    for j in range(w):
        if S[i + 1][j] == '#':
            if S[i][j] !='#':
                S[i][j] += 1

for i in range(h - 1):
    for j in range(w):
        if S[i][j] == '#' and S[i + 1][j] != '#':
            S[i + 1][j] += 1

for i in range(h):
    for j in range(w - 1):
        if S[i][j] == '#' and S[i][j + 1] != '#':
            S[i][j + 1] += 1

for i in range(h):
    for j in range(w - 1):
        if S[i][j + 1] == '#' and S[i][j] !='#':
            S[i][j] += 1

for i in range(h - 1):
    for j in range(w - 1):
        if S[i][j] == '#' and S[i + 1][j + 1] != '#':
            S[i + 1][j + 1] += 1

for i in range(h - 1):
    for j in range(1, w):
        if S[i][j] == '#' and S[i + 1][j - 1] != '#':
            S[i + 1][j - 1] += 1

for i in range(1, h):
    for j in range(w - 1):
        if S[i][j] == '#' and S[i - 1][j + 1] != '#':
            S[i - 1][j + 1] += 1

for i in range(1, h):
    for j in range(1, w):
        if S[i][j] == '#' and S[i - 1][j - 1] != '#':
            S[i - 1][j - 1] += 1

for i in range(h):
    s = S[i]
    t = ''
    for j in range(w):
        x = str(s[j])
        t += x
    print(t)



