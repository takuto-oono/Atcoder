def main():
    n = int(input())
    a_list = []
    for i in range(n):
        a = list(map(int, input().split()))
        a_list.append(a)

    a_list.sort()
    ans = n
    for i in range(n - 1):
        if a_list[i][0] != a_list[i + 1][0]:
            continue

        judgement = True
        for j in range(min(a_list[i][0], a_list[i + 1][0])):
            if a_list[i][j + 1] == a_list[i + 1][j + 1]:
                continue

            judgement = False
            break

        if judgement:
            ans -= 1

    print(ans)


if __name__ == '__main__':
    main()
