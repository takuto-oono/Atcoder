from typing import List


def operate(a_list: List[int], l: int, n: int, k: int) -> List[int]:
    if a_list[l - 1] == n:
        return a_list

    if l == k:
        a_list[l - 1] += 1
        return a_list

    if a_list[l - 1] + 1 == a_list[l]:
        return a_list

    a_list[l - 1] += 1
    return a_list


def main():
    n, k, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    l_list = list(map(int, input().split()))
    for l in l_list:
        a_list = operate(a_list, l, n, k)
    print(*a_list)


if __name__ == '__main__':
    main()
