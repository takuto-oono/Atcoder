from typing import List


def create_list_cumulative_sum(a_list: List[int]) -> List[int]:
    cumulative_sum_list = [0 for _ in range(len(a_list))]
    s = 0
    for i, a in enumerate(a_list):
        s += a
        cumulative_sum_list[i] = s
    return cumulative_sum_list


def count_do_a_list_max(a_list: List[int]) -> int:
    cnt = 0
    a_max = a_list[-1]
    for a in a_list:
        cnt += a_max - a
    return cnt


def count_do_a_list_min(a_list: List[int]) -> int:
    cnt = 0
    a_min = a_list[0]
    for a in a_list:
        cnt += a - a_min
    return cnt


def lower_bound(li: List[int], x: int) -> int:
    l, r = 0, len(li) - 1
    while l <= r:
        m = l + (r - l) // 2
        if li[m] < x:
            l = m + 1
        else:
            r = m - 1
    return l


def ans_query(x: int, a_list: List[int], cumulative_sum_list: List[int], count_do_max: int, count_do_min: int) -> int:
    if x >= a_list[-1]:
        return count_do_max + (x - a_list[-1]) * len(a_list)
    if x <= a_list[0]:
        return count_do_min + (a_list[0] - x) * len(a_list)
    m = lower_bound(a_list, x)
    print(m)
    if a_list[m] == x:
        return x * m - cumulative_sum_list[m - 1] + cumulative_sum_list[-1] - x * len(a_list)
    else:
        return x * (m + 1) - cumulative_sum_list[m] + cumulative_sum_list[-1] - x * len(a_list)


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_list = sorted(a_list)
    cumulative_sum_list = create_list_cumulative_sum(a_list)
    count_do_max = count_do_a_list_max(a_list)
    count_do_min = count_do_a_list_min(a_list)

    for _ in range(q):
        print(ans_query(int(input()), a_list, cumulative_sum_list, count_do_max, count_do_min))


if __name__ == '__main__':
    main()
