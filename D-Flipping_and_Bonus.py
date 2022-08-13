from typing import List, Dict


def exchange_to_dic_counter_and_bonus_list(counter_and_bonus_list: List[List[int]], n: int) -> Dict[int, int]:
    counter_and_bonus_dic = {}
    for i in range(n):
        counter_and_bonus_dic[i + 1] = 0
    for counter_and_bonus in counter_and_bonus_list:
        counter_and_bonus_dic[counter_and_bonus[0]] = counter_and_bonus[1]
    return counter_and_bonus_dic


def dp(getting_money_list: List[int], counter_and_bonus_dic: Dict[int, int], n: int) -> int:
    dp_list = [[-1 for _ in range(n + 1)] for _ in range(n)]
    dp_list[0][0] = 0
    dp_list[0][1] = getting_money_list[0] + counter_and_bonus_dic[1]
    for i in range(n - 1):
        for j in range(n):
            if dp_list[i][j] == -1:
                break
            now_money = dp_list[i][j]
            if j == 0:
                dp_list[i + 1][0] = max(dp_list[i + 1][0], now_money)
                dp_list[i + 1][1] = max(dp_list[i + 1][1],
                                        now_money + getting_money_list[i + 1] + counter_and_bonus_dic[j + 1])
                continue
            dp_list[i + 1][0] = max(dp_list[i + 1][0], now_money)
            dp_list[i + 1][j + 1] = max(dp_list[i + 1][j + 1],
                                        now_money + getting_money_list[i + 1] + counter_and_bonus_dic[j + 1])

    return max(dp_list[n - 1])


def count_max_money(n: int, getting_money_list: List[int], counter_and_bonus_list: List[List[int]]) -> int:
    return dp(getting_money_list, exchange_to_dic_counter_and_bonus_list(counter_and_bonus_list, n), n)


def main():
    n, m = map(int, input().split())
    getting_money_list = list(map(int, input().split()))
    counter_and_bonus_list = []
    for _ in range(m):
        c, y = map(int, input().split())
        counter_and_bonus_list.append([c, y])

    print(count_max_money(n, getting_money_list, counter_and_bonus_list))


if __name__ == '__main__':
    main()
