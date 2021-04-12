w, h, n = map(int, input().split())
Status = [[0 for j in range(w)] for i in range(h)]

for i in range(n):
    x, y, a = map(int, input().split())

    if a == 1:
        for i in range(h):
            for j in range(w):
                if j + 1 <= x:
                    Status[i][j] = 1

    elif a == 2:
        for i in range(h):
            for j in range(w):
                if j + 1 > x:
                    Status[i][j] = 1

    elif a == 3:
        for i in range(h):
            for j in range(w):
                if i + 1 <= y:
                    Status[i][j] = 1

    elif a == 4:
        for i in range(h):
            for j in range(w):
                if i + 1 > y:
                    Status[i][j] = 1

ans = 0
for i in range(h):
    for j in range(w):
        if Status[i][j] == 0:
            ans += 1
print(ans)