from xml.etree.ElementInclude import XINCLUDE


def main():
    n, q = map(int, input().split())
    a_list = list(map(int, input().split()))
    no_duplication_a_list = list(set(a_list))
    a_dic = {}
    for a in no_duplication_a_list:
        a_dic[a] = []
    for index in range(n):
        a_dic[a_list[index]].append(index + 1)
    ans_list = []
    for i in range(q):
        x, k = map(int, input().split())
        if (x in a_dic):
            x_index_list = a_dic[x]
            if len(x_index_list) < k:
                ans = -1
            else:
                ans = x_index_list[k - 1]
        else:
            ans = -1
        ans_list.append(ans)
    for ans in ans_list:
        print(ans)


if __name__ == '__main__':
    main()
