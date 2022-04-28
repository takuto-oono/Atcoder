def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_dic = {}
    for i, a in enumerate(a_list):
        if a in a_dic:
            a_dic[a].append(i)
        else:
            a_dic[a] = [i]

    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        ans = 0
        if x in a_dic:
            ok1 = 0
            ng1 = len(a_dic[x]) - 1

            while ng1 - ok1 > 1:
                mid = (ng1 + ok1) // 2
                if a_dic[x][mid] == l:
                    ok1 = mid
                    break
                elif a_dic[x][mid] < l:
                    ok1 = mid
                else:
                    ng1 = mid

            ok2 = len(a_dic[x]) - 1
            ng2 = 0

            while ok2 - ng2 > 1:
                mid = (ok2 + ng2) // 2
                if a_dic[x][mid] == r:
                    ok2 = mid
                    break
                elif a_dic[x][mid] > r:
                    ok2 = mid
                else:
                    ng2 = mid

            ans = ok2 - ok1 + 1
        print(ans)


if __name__ == '__main__':
    main()
