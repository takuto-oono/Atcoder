def main():
    n, k, x = map(int, input().split())
    a_list = list(map(int, input().split()))

    for i, a in enumerate(a_list):
        if a < x:
            continue

        if a // x <= k:
            a_list[i] = a % x
            k -= a // x
        else:
            a_list[i] = a - x * k
            k = 0
            break
    a_list.sort(reverse=True)
    ans = 0
    for i in range(k, n):
        ans += a_list[i]
    print(ans)


if __name__ == '__main__':
    main()
