from typing import List


def create_cumulative_sum_list(a_list: List[int]) -> List[int]:
    cumulative_sum_list = []
    s = 0
    for a in a_list:
        s += a
        cumulative_sum_list.append(s)
    return cumulative_sum_list


def count_ans(a_list: List[int]) -> int:
    ans = 0
    for cumulative_sum in create_cumulative_sum_list(list(reversed(a_list))):
        if cumulative_sum >= 4:
            ans += 1
    return ans


def main():
    _ = int(input())
    a_list = list(map(int, input().split()))
    print(count_ans(a_list))


if __name__ == '__main__':
    main()
