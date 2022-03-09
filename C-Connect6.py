from typing import List
n = 0
s_list = []


def count_black(list: List) -> bool:
    return list.count('#') >= 4


def judge() -> bool:
    for y in range(n):
        for x in range(n):
            if (y < n - 5) and (x < n - 5):
                if count_black([s_list[y + i][x + i] for i in range(6)]):
                    return True

            if (y < n - 5):
                if count_black([s_list[y + i][x] for i in range(6)]):
                    return True

            if (x < n - 5):
                if count_black([s_list[y][x + i] for i in range(6)]):
                    return True

            if (y >= 5) and (x < n - 5):
                if count_black([s_list[y - i][x + i] for i in range(6)]):
                    return True

    return False


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s_list.append(list(input()))

    if judge():
        print('Yes')
    else:
        print('No')
