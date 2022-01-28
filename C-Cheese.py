def main():
    n, w = map(int, input().split())
    ab_list = []
    for i in range(n):
        a, b = map(int, input().split())
        ab_list.append([a, b])

    ab_list = sorted(ab_list, reverse=True)

    def cal(n, w):
        ans = 0
        for i in range(n):
            if w == 0:
                break

            a = ab_list[i][0]
            b = ab_list[i][1]

            if b <= w:
                w -= b
                ans += a * b
                continue

            if b > w:
                ans += a * w
                w = 0
                continue

        return ans

    ans = cal(n, w)
    print(ans)


if __name__ == '__main__':
    main()
