





def main():
    n, x = map(int, input().split())
    
    def leveln(n):
        if n == 0:
            return 'p'
        
        dp = ['' for _ in range(n + 1)]
        dp[0] = 'p'
        
        for i in range(1, n + 1):
            dp[i] = 'b' + dp[i - 1] + 'p' + dp[i - 1] + 'b'
        
        return dp[n]
    
    bagas = leveln(n)
    ans = 0
    co = 0
    for baga in bagas:
        co += 1
        if baga == 'p':
            ans += 1
        
        if co == x:
            break

    print(ans)
    
if __name__ == '__main__':
    main()
