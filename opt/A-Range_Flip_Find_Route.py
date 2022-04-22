h, w = map(int, input().split())

S = []
for i in range(h):
    s = list(input())
    S.append(s)

D = [[0 for j in range(w)] for i in range(h)]

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0 and S[0][0] == '#':
            D[0][0] = 1

        elif i == 0:
            left = D[i][j - 1]
            if S[i][j - 1] != S[i][j]:
                left += 1
            D[i][j] = left

        elif j == 0:
            up = D[i - 1][j]
            if S[i - 1][j] != S[i][j]:
                up += 1
            D[i][j] = up

        else:
            left = D[i][j - 1]
            up = D[i - 1][j]
            if S[i][j - 1] != S[i][j]:
                left += 1
            if S[i - 1][j] != S[i][j]:
                up += 1

            D[i][j] = min(up, left)

            if i == h - 1 and j == w - 1 and S[i][j] == '#':
                D[i][j] += 1











ans = D[h - 1][w - 1] // 2
print(ans)

