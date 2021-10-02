





def Initial_setting(a, M):
    M[a] = 1
    return M

def Operation_execution(A, M):
    for i in range(len(A)):
        if i == 0:
            M = Initial_setting(A[i], M)

        else:
            a = A[i]
            M_change_count = [0 for _ in range(10)]
            for j in range(len(M)):
                m = M[j]
                x = j

                if m == 0:
                    continue

                s = (a + x) % 10
                p = (a * x) % 10
                M_change_count[s] += m
                M_change_count[p] += m
                M_change_count[j] -= m

            for j in range(len(M)):
                M[j] = (M_change_count[j] + M[j]) % 998244353

    return M

def Print_ans(M):
    for ans in M:
        print(ans % 998244353)

def main():
    n = int(input())
    A = list(map(int, input().split()))
    M = [0 for _ in range(10)]
    M = Operation_execution(A, M)
    Print_ans(M)

main()


