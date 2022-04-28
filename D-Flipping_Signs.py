





def dynamic_programming(A, n):
    dp = [[0, 0] for _ in range(n + 1)]
    dp[0][1] = -1000000000000000000
    for i in range(n):
        a = A[i]
        dp[i + 1][0] = max(dp[i][0] + a, dp[i][1] - a)
        dp[i + 1][1] = max(dp[i][1] + a, dp[i][0] - a)
    
    return dp[n][0]


def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(dynamic_programming(A, n))

main()




