import sys
from typing import List, Generator

sys.setrecursionlimit(1000000)

A_LIST = []
IS_USED = {k: False for k in range(1, 17)}


def access_a_list(pairs: List[List[int]]) -> Generator[int, None, None]:
    for pair in pairs:
        yield A_LIST[pair[0] - 1][pair[1] - pair[0] - 1]


def xor(value_list: List[int]) -> int:
    result = 0
    for v in value_list:
        result ^= v
    return result


def full_search(n: int, pairs: List[List[int]]) -> int:
    if len(pairs) == n:
        return xor([a for a in access_a_list(pairs)])
    p1 = 0
    for i in range(1, 2 * n + 1):
        if not IS_USED[i]:
            p1 = i
            break
    IS_USED[p1] = True

    max_xor = 0
    for i in range(1, 2 * n + 1):
        if not IS_USED[i]:
            pairs.append([p1, i])
            IS_USED[i] = True
            max_xor = max(max_xor, full_search(n, pairs))
            pairs.pop(-1)
            IS_USED[i] = False

    IS_USED[p1] = False
    return max_xor


def main():
    n = int(input())
    for _ in range(2 * n - 1):
        A_LIST.append(list(map(int, input().split())))
    print(full_search(n, []))


if __name__ == '__main__':
    main()
