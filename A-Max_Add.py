





def F(n, A):
    A_max = A[0]
    A_sum = A[0]
    ans = A_max + A_sum

    for i in range(n):
        if i == 0:
            print(ans)

        else:
            A_sum += A[i]
            ans += A_sum - A_max * i
            A_max = max(A_max, A[i])
            ans += A_max * (i + 1)
            print(ans)

def main():
    n = int(input())
    A = list(map(int, input().split()))
    F(n, A)

main()

