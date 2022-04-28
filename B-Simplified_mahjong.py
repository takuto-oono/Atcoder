n = 0
a_list = []


def create_pair() -> None:
    ans = 0

    for i, a in enumerate(a_list):
        if i == n - 1:
            ans += a // 2
            break

        if a >= 2:
            ans += a // 2
            a_list[i] = a % 2

        m = min(a_list[i], a_list[i + 1])
        ans += m
        a_list[i] -= m
        a_list[i + 1] -= m

    print(ans)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        a_list.append(a)

    create_pair()
