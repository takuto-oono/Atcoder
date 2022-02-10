def dfs(n, branch, start, seen_list):
    todo_list = []
    if seen_list[start] == False:
        seen_list[start] = True
        todo_list.append(start)

    while(len(todo_list) > 0):
        todo = todo_list.pop(0)
        for b in branch[todo]:
            if seen_list[b]:
                return False

            seen_list[b] = True
            todo_list.append(b)

    return True


def judge(n, branch, ab_list):
    max_len = 0
    for b in branch:
        max_len = max(max_len, len(b))

    if max_len > 2:
        return False

    seen_list = [False for _ in range(n)]
    for start in ab_list:
        judgement = dfs(n, branch, start, seen_list)
        print(seen_list)
        if judgement:
            continue

        return False

    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    branch = [[] for _ in range(n)]
    ab_list = []
    count_list = [0 for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        count_list[a] += 1
        count_list[b] += 1

        branch[a].append(b)
        branch[b].append(a)
        ab_list.append(a)
        ab_list.append(b)

    if max(count_list) > 2:
        print('No')
        exit()

    ab_list = list(set(ab_list))

    if judge(n, branch, ab_list):
        print('Yes')

    else:
        print('No')
