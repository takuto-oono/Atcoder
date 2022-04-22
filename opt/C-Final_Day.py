def main():
    n, k = map(int, input().split())
    score_list = []
    for i in range(n):
        p_list = list(map(int, input().split()))
        score_list.append([sum(p_list), i])

    score_list.sort(reverse=True)
    ans_list = [False for _ in range(n)]
    score_k = score_list[k - 1][0]
    for i in range(n):
        if i <= k:
            ans_list[score_list[i][1]] = True
            continue

        if score_list[i][0] + 300 >= score_k:
            ans_list[score_list[i][1]] = True
            continue

    for i in range(n):
        if ans_list[i]:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
