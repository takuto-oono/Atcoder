from typing import List
n = 0
s_list = []


def count_black(color_list: List[int]) -> bool:
    cnt = 0
    for color in color_list:
        if color == '#':
            cnt += 1

    return cnt >= 4


def judge():
    for y in range(n):
        for x in range(n):
            if y <= n - 6:
                if count_black([s_list[y + i][x] for i in range(6)]):
                    return True

            if x <= n - 6:
                if count_black([s_list[y][x + i] for i in range(6)]):
                    return True

            if y <= n - 6 and x <= n - 6:
                if count_black([s_list[y + i][x + i] for i in range(6)]):
                    return True

            if y <= n - 6 and x < 6:
                if count_black([s_list[y + i][x - i] for i in range(6)]):
                    return True
    return False


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = list(input())
        s_list.append(s)

    if judge():
        print('Yes')
    else:
        print('No')
