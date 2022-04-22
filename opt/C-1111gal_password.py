n = 0
m = 998244353


def full_search():
    dp = [[0 for _ in range(9)] for _ in range(n)]
    for i in range(9):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(9):
            if j == 0:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % m
            elif j == 8:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % m
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % m

    return sum(dp[n - 1]) % m


if __name__ == '__main__':
    n = int(input())
    print(full_search())
