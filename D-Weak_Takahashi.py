





def main():
    h, w = map(int, input().split())
    C = []
    for i in range(h):
        c = list(input())
        C.append(c)
    
    dp = [[False for _ in range(w)] for _ in range(h)]
    
    ans = 1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                dp[i][j] = True
                continue
            
            if C[i][j] == '#':
                continue
            
            if j > 0:
                if dp[i][j - 1]:
                    dp[i][j] = True
                    ans = max(i + j + 1, ans)
            
            if i > 0:
                if dp[i - 1][j]:
                    dp[i][j] = True
                    ans = max(i + j + 1, ans)
    
    print(ans)
    
if __name__ == '__main__':
    main()

            