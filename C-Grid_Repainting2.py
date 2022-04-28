h, w = map(int,input().split())
S = []
for i in range(h):
    s = input()
    S.append(s)

for i in range(h):
    for j in range(w):
        if S[i][j] == '#':
            co = 0
            if i != 0:
                if S[i - 1][j] == '#':
                    co += 1
            if i != h - 1:
                if S[i + 1][j] == '#':
                    co += 1
            if j != 0:
                if S[i][j - 1] == '#':
                    co += 1
            if j != w - 1:
                if S[i][j + 1] == '#':
                    co += 1
            if co == 0:
                print('No')
                exit()

print('Yes')
