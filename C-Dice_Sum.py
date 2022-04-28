def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    dp_list = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    dp_list[0][0] = 1
    for i in range(n):
        for j in range(k):
            for l in range(1, m + 1):
                if j + l <= k:
                    dp_list[i + 1][j + l] += dp_list[i][j]
    ans = 0
    for i in range(k + 1):
        ans += dp_list[n][i] % mod
    print(ans % mod)


if __name__ == '__main__':
    main()
