ans_candidate_dic = {}


def factorization(x):
    y = x
    for i in range(2, int(y ** 0.5) + 1):
        if x % i == 0:
            ans_candidate_dic[i] = False
            while x % i == 0:
                x //= i

    if x != 1:
        ans_candidate_dic[x] = False


def delete_multiple(m):
    for key in ans_candidate_dic:
        value = ans_candidate_dic[key]
        if value:
            continue

        x = 2 * key
        while(x <= m):
            ans_candidate_dic[x] = False
            x += key


def print_ans():
    ans_count = 0
    for key in ans_candidate_dic:
        if ans_candidate_dic[key]:
            ans_count += 1

    print(ans_count)

    for key in ans_candidate_dic:
        if ans_candidate_dic[key]:
            print(key)


if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    for i in range(1, m + 1):
        ans_candidate_dic[i] = True

    for a in a_list:
        factorization(a)

    delete_multiple(m)

    print_ans()
