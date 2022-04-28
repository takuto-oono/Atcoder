a_list = []
ans_list = []
if __name__ == '__main__':
    n = int(input())
    a_list = list(map(int, input().split()))
    ans_list = []
    flag = False
    cnt = 0
    k = a_list[0]
    ans = 0
    count_list = []
    for i, a in enumerate(a_list):
        ans += 1
        if a == k:
            cnt += 1
            if cnt == k:
                ans -= k
                if len(count_list) > 0:
                    k = count_list[-1][0]
                    cnt = count_list[-1][1]
                    count_list.pop(-1)
                else:
                    k = -1
                    cnt = 0
        else:
            if k != -1:
                count_list.append([k, cnt])
            cnt = 1
            k = a

        print(ans)
