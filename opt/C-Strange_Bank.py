





def main():
    n = int(input())
    ans = 0
    list_a = []
    list_b = []
    i = -1
    while(6 ** (i + 1) <= n):
        list_a.append(6 ** (i + 1))
        i += 1

    i = -1
    while(9 ** (i + 1) <= n):
        list_b.append(9 ** (i + 1))
        i += 1
        
    list_bank = list_a + list_b
    list_bank.sort()
    
    dp = [10 ** 9 for _ in range(n + 1)]
    dp[0] = 0
    
    for i in range(1, n + 1):
        for bank in list_bank:
            if i - bank < 0:
                break

            dp[i] = min(dp[i], dp[i - bank] + 1)
    
    ans = dp[n]
    print(ans)
    
if __name__ == '__main__':
    main()
