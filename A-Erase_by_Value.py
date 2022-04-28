def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    x = a_list[-1]
    for i in range(n - 1):
        if a_list[i] > a_list[i + 1]:
            x = a_list[i]
            break

    ans_list = [a for a in a_list if a != x]

    print(*ans_list)


if __name__ == '__main__':
    main()
