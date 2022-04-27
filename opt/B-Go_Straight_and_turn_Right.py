def main():
    n = int(input())
    t_list = list(input())
    ans = [0, 0]
    dir_list = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    dir = 0
    for t in t_list:
        if t == 'S':
            ans[0] += dir_list[dir % 4][0]
            ans[1] += dir_list[dir % 4][1]
        if t == 'R':
            dir += 1

    print(ans[0], ans[1])


if __name__ == '__main__':
    main()
