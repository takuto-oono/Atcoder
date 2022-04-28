import sys
sys.setrecursionlimit(10 ** 8)

branch_dic = {}
x_list = []
import heapq


def delete_par(par):
    for child in branch_dic[par]:
        branch_dic[child].remove(par)
        delete_par(child)


def dfs(par, top_list, k, flag):
    x = x_list[par - 1]
    top_list.append(x)
    
    if flag:
        top_list.append
        top_list = heapq.nlargest(k, top_list)

    else:
        if len(top_list) == k:
            flag = True

    for child in branch_dic[par]:
        dfs(child, top_list, k, False)


def process_query(v, k):
    top_list = []
    dfs(v, top_list, k, False)
    print(top_list)


if __name__ == "__main__":
    n, q = map(int, input().split())
    x_list = list(map(int, input().split()))
    for i in range(n):
        branch_dic[i + 1] = []

    for i in range(n - 1):
        a, b = map(int, input().split())
        branch_dic[a].append(b)
        branch_dic[b].append(a)

    delete_par(1)

    for _ in range(q):
        v, k = map(int, input().split())
        process_query(v, k)
