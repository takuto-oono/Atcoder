N = int(input())
A = list(input().split())
ans = 0
for i in range(N):
    if i + 1 == A.index(A[i] - 1):
        ans += 1

ans = ans // 2
print(ans)


