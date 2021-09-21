





def list_sum(S):
    A = []
    for i in range(len(S)):
        c = 0
        for j in range(len(S[i])):
            c += int(S[i][j])
        A.append(c % 2)
    return A

def print_ans(S_sum_list):
    c_0 = 0
    c_1 = 0
    for i in S_sum_list:
        if i == 0:
            c_0 += 1
        else:
            c_1 += 1

    ans = c_0 * c_1
    print(ans)

def main():
    n, m = map(int, input().split())
    S = []
    for i in range(n):
        s = list(input())
        S.append(s)

    S_sum_list = list_sum(S)

    print_ans(S_sum_list)

main()




