import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
A, N = map(int, input().split())


def process():
    m = 1
    while (m <= N):
        m *= 10
    seen_list = [-1 for _ in range(m + 1)]
    seen_list[1] = 0
    todo_list = deque()
    todo_list.append(1)
    while todo_list:
        x = todo_list.popleft()
        p = seen_list[x]
        op1 = x * A
        if op1 < m and seen_list[op1] == -1:
            todo_list.append(op1)
            seen_list[op1] = p + 1

        if x >= 10 and x % 10 != 0:
            x_str = str(x)
            op2 = int(x_str[-1] + x_str[:len(x_str) - 1])
            if op2 < m and seen_list[op2] == -1:
                todo_list.append(op2)
                seen_list[op2] = p + 1
    return seen_list[N]


if __name__ == '__main__':
    print(process())
