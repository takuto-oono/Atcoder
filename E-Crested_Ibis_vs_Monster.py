





def main():
    h, n = map(int, input().split())
    ab_list = []
    for i in range(n):
        a, b = map(int, input().split())
        ab_list.append([a, b])
        
    dp = [[10 ** 9 for _ in range(h + 10)] for _ in range(n + 10)]
    
    dp[0][h] = 0
    
    for i in range(n):
        for j in reversed(range(h + 1)):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            dp[i][max(0, j - ab_list[i][0])] = min(dp[i][max(0, j - ab_list[i][0])], dp[i][j] + ab_list[i][1])
            
    ans = dp[n][0]
    print(ans)
        
if __name__ == '__main__':
    main()

            