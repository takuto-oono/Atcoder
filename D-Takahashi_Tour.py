import sys
sys.setrecursionlimit(10 ** 8)


branch_dic = {}
location_list = []


def dfs(current, previous):
    location_list.append(current)

    for next in branch_dic[current]:
        if next != previous:
            dfs(next, current)
            location_list.append(current)


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        branch_dic[i + 1] = []

    for i in range(n - 1):
        a, b = map(int, input().split())
        branch_dic[a].append(b)
        branch_dic[b].append(a)

    for key in range(1, n + 1):
        branch_dic[key].sort()

    dfs(1, -1)
    print(*location_list)
