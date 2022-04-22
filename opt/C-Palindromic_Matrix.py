from typing import List

h = 0
w = 0
a_count_list = [0 for _ in range(26)]


def change_int_from_str(c: str) -> int:
    return ord(c) - 97


def judge_even_even() -> bool:
    for count in a_count_list:
        if count % 4 != 0:
            return False

    return True


def create_not_4_count_list() -> List[int]:
    not_4_count_list = [0 for _ in range(26)]
    for index, count in enumerate(a_count_list):
        if count % 4 != 0:
            not_4_count_list[index] = count % 4
            a_count_list[index] -= count % 4

    return not_4_count_list


def judge_1(n: int) -> bool:
    if n % 2 == 0:
        for count in a_count_list:
            if count % 2 == 1:
                return False

    else:
        odd_cnt = 0
        for count in a_count_list:
            if count % 2 == 1:
                odd_cnt += 1
                if odd_cnt == 2:
                    return False

    return True


def judge_odd_odd() -> bool:
    not_4_count_list = create_not_4_count_list()
    if sum(not_4_count_list) > h + w - 1:
        return False

    cnt = 0
    for count in not_4_count_list:
        if count % 2 != 0:
            cnt += 1
            if cnt == 2:
                return False

    if cnt == 0:
        return False

    if sum(not_4_count_list) < h + w - 1:
        if h + w - 1 - sum(not_4_count_list) % 4 != 0:
            return False

    return True


def judge_odd_even(even_num: int) -> bool:
    not_4_count_list = create_not_4_count_list()

    if sum(not_4_count_list) > even_num:
        return False

    for count in not_4_count_list:
        if count % 2 == 1:
            return False

    if sum(not_4_count_list) < even_num:
        if even_num - sum(not_4_count_list) % 4 != 0:
            return False

    return True


def judge(h: int, w: int) -> bool:

    if h == 1 or w == 1:
        if h == 1 and w == 1:
            return True

        if h == 1:
            return judge_1(w)

        if w == 1:
            return judge_1(h)

    if h % 2 == 0 and w % 2 == 0:
        return judge_even_even()

    if h % 2 == 1 and w % 2 == 1:
        return judge_odd_odd()

    if h % 2 == 0:
        return judge_odd_even(h)

    return judge_odd_even(w)


if __name__ == '__main__':
    h, w = map(int, input().split())
    for _ in range(h):
        a_list = list(input())
        for a in a_list:
            a_count_list[change_int_from_str(a)] += 1

    if judge(h, w):
        print('Yes')
    else:
        print('No')
