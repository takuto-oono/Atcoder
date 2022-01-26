def main():
    n, m = map(int, input().split())
    s_list = list(input().split())
    t_list = list(input().split())
    ans_list = []
    j = 0
    for i in range(m):
        while(j < n):
            if (s_list[j] == t_list[i]):
                j += 1
                ans_list.append(True)
                break

            ans_list.append(False)
            j += 1
    for ans in ans_list:
        if ans:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
