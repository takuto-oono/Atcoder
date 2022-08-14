from typing import List, Generator


def find_min_a_list_sum(a_list: List[int], l: int, r: int) -> int:
    dp_list = [[10 ** 18 for _ in range(3)] for _ in range(len(a_list))]
    dp_list[0][0] = l
    dp_list[0][1] = a_list[0]
    dp_list[0][2] = r

    for i in range(len(a_list) - 1):
        now_sum = dp_list[i][0]
        dp_list[i + 1][0] = min(dp_list[i + 1][0], now_sum + l)
        dp_list[i + 1][1] = min(dp_list[i + 1][1], now_sum + a_list[i + 1])
        dp_list[i + 1][2] = min(dp_list[i + 1][2], now_sum + r)

        now_sum = dp_list[i][1]
        dp_list[i + 1][1] = min(dp_list[i + 1][1], now_sum + a_list[i + 1])
        dp_list[i + 1][2] = min(dp_list[i + 1][2], now_sum + r)

        now_sum = dp_list[i][2]
        dp_list[i + 1][2] = min(dp_list[i + 1][2], now_sum + r)

    return min(dp_list[-1])


def main():
    n, l, r = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(find_min_a_list_sum(a_list, l, r))


if __name__ == '__main__':
    main()
