def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    s_list = [0]
    cnt = 0
    for i in range(n):
        cnt += a_list[i]
        s_list.append(cnt)

    s_dic = {}
    for i in range(len(s_list)):
        s = s_list[i]
        if s in s_dic:
            s_dic[s].append(i)
            continue

        if s not in s_dic:
            s_dic[s] = [i]
            continue

    ans = 0

    for i in range(len(s_list)):
        s = s_list[i]
        if s - k in s_dic:
            for index in s_dic[s - k]:
                if index < i:
                    ans += 1

    print(ans)


if __name__ == '__main__':
    main()
