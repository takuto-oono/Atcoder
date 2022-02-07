def main():
    abc_string = input()
    x_list_list = [[0, 1, 2], [1, 2, 0], [2, 0, 1]]

    def create(abc_string, x_list):
        x = 0
        for i in range(3):
            x += 10 ** (3 - i - 1) * int(abc_string[x_list[i]])

        return x

    x = create(abc_string, x_list_list[0])
    y = create(abc_string, x_list_list[1])
    z = create(abc_string, x_list_list[2])

    ans = x + y + z

    print(ans)


if __name__ == '__main__':
    main()
