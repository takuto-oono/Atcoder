import sys
from typing import List, Generator


def cal_cumulative_sum_a_and_b_list(n: int, a_list: List[int], b_list: List[int]) -> Generator[int, None, None]:
    result = 0
    for i in range(n):
        result += a_list[i] + b_list[i]
        yield result


def find_min_values_in_b_list(b_list: List[int]) -> Generator[int, None, None]:
    b_min = 10 ** 17
    for b in b_list:
        b_min = min(b, b_min)
        yield b_min


def cal_time_x_stage_completed_full_search(x: int, n: int, a_list: List[int], b_list: List[int]) -> int:
    cumulative_sum_a_and_b_list = [s for s in cal_cumulative_sum_a_and_b_list(n, a_list, b_list)]
    b_list_min_values_list = [b for b in find_min_values_in_b_list(b_list)]
    result = sys.maxsize
    for i in range(n):
        remaining_x = x - (i + 1)
        if remaining_x < 0:
            break
        b_min = b_list_min_values_list[i]
        result = min(result, cumulative_sum_a_and_b_list[i] + b_min * remaining_x)
    return result


def main():
    n, x = map(int, input().split())
    a_list, b_list = [], []
    for i in range(n):
        a, b = map(int, input().split())
        a_list.append(a)
        b_list.append(b)
    print(cal_time_x_stage_completed_full_search(x, n, a_list, b_list))


if __name__ == '__main__':
    main()
