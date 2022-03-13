xy_list = []


def main():
    n = int(input())
    for i in range(n):
        xy_list.append(list(map(int, input().split())))
    s_string = input()
    left_dic = {}
    right_dic = {}
    for i in range(n):
        x = xy_list[i][0]
        y = xy_list[i][1]
        dir_i = s_string[i]
        if dir_i == "L":
            if y in left_dic:
                left_dic[y].append(x)
            else:
                left_dic[y] = [x]
        else:
            if y in right_dic:
                right_dic[y].append(x)
            else:
                right_dic[y] = [x]
    flag_collision = False
    for y in left_dic:
        if y not in right_dic:
            continue

        if min(right_dic[y]) <= max(left_dic[y]):
            flag_collision = True
            break

    if flag_collision:
        print('Yes')
    else:
        print("No")


if __name__ == '__main__':
    main()
