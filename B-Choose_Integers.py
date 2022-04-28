a, b, c = map(int,input().split())
A = [i * a for i in range(1, 10 ** 2 + 3)]
for i in range(10 ** 2 - 1 + 3):
    A[i] %= b
A = list(set(A))

n = len(A)
s = sum(A)
if s < c:
    print('NO')
    exit()


dp =[[0 for j in range(s + 1)] for i in range(n + 1)]
dp[0][0] = 1


for i in range(n):
    for j in range(s + 1):
        if j - A[i] >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - A[i]])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])




for i in range(n + 1):
    if dp[i][c] == 1:
        print('YES')
        exit()
print('NO')