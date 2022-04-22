N = int(input())
AB_list = []
for _ in range(N):
    AB_list.append(list(map(int, input().split())))


def main():
    sum_time = 0
    for i in range(N):
        sum_time += AB_list[i][0] / AB_list[i][1]

    sum_time /= 2
    ans = 0
    for i in range(N):
        a = AB_list[i][0]
        b = AB_list[i][1]
        if sum_time > a / b:
            sum_time -= a / b
            ans += a

        else:
            ans += sum_time * b
            break

    print(ans)


if __name__ == '__main__':
    main()
