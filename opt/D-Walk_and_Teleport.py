





def main():
    n, a, b = map(int, input().split())
    x_list = list(map(int, input().split()))
    
    dp = [10 ** 10 for _ in range(n)]
    dp[0] = 0
    
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + b, dp[i - 1] + a * (x_list[i] - x_list[i - 1]))
    
    ans = dp[n - 1]
    print(ans)
    
if __name__ == '__main__':
    main()
        