def main():
    n, m, x, t, d = map(int, input().split())
    if 0 <= m <= x:
        ans = t - d * (x - m)
    else:
        ans = t
    print(ans)


if __name__ == '__main__':
    main()
