q = 0
a_list = []


def binary_search(x: int) -> int:
    left = 0
    right = len(a_list)
    if x <= a_list[0]:
        return 0

    if x >= a_list[-1]:
        return len(a_list)

    while right - left > 1:
        mid = (right + left) // 2
        if a_list[mid] <= x:
            left = mid
        else:
            right = mid

    return left


def process1(x: int) -> None:
    if len(a_list) == 0:
        a_list.append(x)
        return
    index = binary_search(x)
    a_list.insert(index, x)


def process2(x: int, k: int) -> int:
    for i in reversed(range(len(a_list))):
        if a_list[i] <= x:
            if i - k + 1 >= 0:
                return a_list[i - k + 1]
            else:
                return -1

    return -1


def process3(x: int, k: int) -> int:
    for i, a in enumerate(a_list):
        if a >= x:
            if i + k - 1 <= len(a_list) - 1:
                return a_list[i + k - 1]
            else:
                return -1

    return -1


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        query_list = list(map(int, input().split()))
        if query_list[0] == 1:
            process1(query_list[1])

        if query_list[0] == 2:
            print(process2(query_list[1], query_list[2]))

        if query_list[0] == 3:
            print(process3(query_list[1], query_list[2]))
