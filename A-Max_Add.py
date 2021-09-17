





def f(A, C, x):

    return C[x] + max(A[:x + 1]) * (x + 1)


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(n)]
    for i in range(n):
        if i == 0:
            B[0] = A[0]

        else:
            B[i] = B[i - 1] + A[i]

    C = [0 for i in range(n)]

    for i in range(n):
        if i == 0:
            C[0] = B[0]

        else:
            C[i] = C[i - 1] + B[i]


    for i in range(n):

        ans = f(A, C, i)
        print(ans)





main()
