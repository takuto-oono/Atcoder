

def main():
    n, x = map(int, input().split())
    a_list = []
    for i in range(n):
        a = list(map(int, input().split()))
        a.pop(0)
        a_list.append(a)
    ans = 0
    output_list = []

    def dfs(a_list, current, i, x, n):
        if (i == n):
            output_list.append(current)
        else:
            for a in a_list[i]:
                dfs(a_list, current * a, i + 1, x, n)

    dfs(a_list, 1, 0, x, n)

    for output in output_list:
        if output == x:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
