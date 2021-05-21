n, m = map(int, input().split())
mod = 10 ** 9 + 7
dp = [0 for i in range(n + 1)]
for i in range(m):
    a = int(input())
    dp[a] = -1

dp[0] = 1
for i in range(1, n + 1):
    if dp[i] == -1:
        continue
    elif i == 1:
        dp[i] = 1
    else:
        if dp[i - 1] == -1 and dp[i - 2] == -1:
            print(0)
            exit()
        elif dp[i - 1] == -1:
            dp[i] = dp[i - 2]
        elif dp[i - 2] == -1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod

print(dp[n] % mod)


