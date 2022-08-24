import sys

sys.setrecursionlimit(10 ** 8)

N = int(input())
TREE = [[] for _ in range(N)]
LR_LIST = [[0, 0] for _ in range(N)]
IS_USED = [False for _ in range(N)]
INIT_VALUE = 1


def print_ans() -> None:
    for (l, r) in LR_LIST:
        print(str(l) + ' ' + str(r))


def create_lr_list(now_node: int):
    global INIT_VALUE
    is_all_used = True
    IS_USED[now_node] = True
    for next_node in TREE[now_node]:
        if not IS_USED[next_node]:
            is_all_used = False
            create_lr_list(next_node)

    if is_all_used:
        LR_LIST[now_node] = [INIT_VALUE, INIT_VALUE]
        INIT_VALUE += 1
        return

    l, r = 100000000, 0
    for next_node in TREE[now_node]:
        if LR_LIST[next_node] == [0, 0]:
            continue
        l = min(l, LR_LIST[next_node][0])
        r = max(r, LR_LIST[next_node][1])
    LR_LIST[now_node] = [l, r]


def main():
    for _ in range(N - 1):
        v, r = map(int, input().split())
        v -= 1
        r -= 1
        TREE[v].append(r)
        TREE[r].append(v)
    create_lr_list(0)
    print_ans()


if __name__ == '__main__':
    main()
