N = int(input())
A = list(map(int,input().split()))
m = 10 ** 18
ans = 1
if 0 in A:
    print(0)
else:
    for i in range(N):
        if A[i] >= m:
            print(-1)
            exit()
    A = sorted(A)
    A = reversed(A)
    for i in A:
        ans *= i
        if ans > m:
            ans = -1
            break
    print(ans) 





