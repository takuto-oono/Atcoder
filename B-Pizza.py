def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = [0, 360]
    sum = 0
    for i in range(n):
        sum += a_list[i]
        sum %= 360
        b_list.append(sum)

    b_list.sort()

    ans = 0
    for i in range(n + 1):
        ans = max(ans, b_list[i + 1] - b_list[i])

    print(ans)


if __name__ == '__main__':
    main()
