def main():
    s_string = input()
    register = [0 for _ in range(10)]
    for s in s_string:
        register[int(s)] = 1

    for i in range(10):
        if register[i]:
            continue

        print(i)


if __name__ == '__main__':
    main()
