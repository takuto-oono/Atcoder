def create_a_sum_list(a_list, n):
    a_sum_list = [0]
    sum = 0
    for a in a_list:
        sum += a
        a_sum_list.append(sum)

    return a_sum_list


def count_gap_k_index_pair(a_sum_list, n, k):
    ans = 0
    a_sum_dic = {}

    for i in range(1, n + 1):
        if a_sum_list[i - 1] in a_sum_dic:
            a_sum_dic[a_sum_list[i - 1]] += 1

        else:
            a_sum_dic[a_sum_list[i - 1]] = 1

        if a_sum_list[i] - k in a_sum_dic:
            ans += a_sum_dic[a_sum_list[i] - k]
    return ans


if __name__ == '__main__':
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(count_gap_k_index_pair(create_a_sum_list(a_list, n), n, k))
