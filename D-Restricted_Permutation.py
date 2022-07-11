from typing import List
import heapq


def create_list_front_num(ab_list: List[List[int]], n: int) -> List[int]:
    front_cnt_list = [0 for _ in range(n)]
    for ab in ab_list:
        front_cnt_list[ab[1]] += 1
    return front_cnt_list


def create_ans_list(ab_list: List[List[int]], n: int) -> List[int]:
    todo = []
    heapq.heapify(todo)
    front_nums_list = create_list_front_num(ab_list, n)
    for i, cnt in front_nums_list:
        if cnt == 0:
            heapq.heappush(i)

    while len(todo) > 0:
        mi = heapq.heappop(todo)








def main():
    n, m = map(int, input().split())
    ab_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        ab_list.append([a - 1, b - 1])


if __name__ == '__main__':
    main()