def main():
    n, x = map(int, input().split())
    s_string = input()
    s_list = []
    for s in s_string:
        if len(s_list) == 0:
            s_list.append(s)
            continue

        if s == 'U' and (s_list[-1] == 'R' or s_list[-1] == 'L'):
            s_list.pop()
        else:
            s_list.append(s)

    for s in s_list:
        if s == 'U':
            x //= 2
        elif s == 'L':
            x *= 2
        else:
            x = x * 2 + 1

    print(x)


if __name__ == '__main__':
    main()
