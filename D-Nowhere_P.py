if __name__ == '__main__':
    n, p = map(int, input().split())
    m = 10 ** 9 + 7
    ans = (p - 1) * pow(p - 2, n - 1, m) % m
    print(ans)
