import bisect


def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_dic = {}
    for i, a in enumerate(a_list):
        if a in a_dic:
            a_dic[a].append(i + 1)
        else:
            a_dic[a] = [i + 1]

    q = int(input())
    for _ in range(q):
        l, r, x = map(int, input().split())
        if x not in a_dic:
            print(0)
            continue

        ans = bisect.bisect_right(
            a_dic[x], r) - bisect.bisect_left(a_dic[x], l)
        print(ans)


if __name__ == '__main__':
    main()
