
def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 10 ** 10
    memo = 0
    for i in range(n):
        for j in range(memo, m):
            if B[j] < A[i]:
                ans = min(ans, abs(A[i] - B[j]))
                memo = j
            else:
                ans = min(ans, abs(A[i] - B[j]))
                memo = j
                break

    print(ans)

main()




