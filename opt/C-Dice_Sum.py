M = 998244353


def main():
    n, m, k = map(int, input().split())
    ans = 1
    for s in range(n + 1, k + 1):
        cnt = 0
        memo = 1
        while(cnt < s - n):
            memo *= n
            ans %= M
            cnt += 1
        print(memo)
        ans += memo
        ans %= M

    print(ans)


if __name__ == '__main__':
    main()
