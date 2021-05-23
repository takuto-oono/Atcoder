n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

BC = [0 for i in range(n)]
for i in range(n):
    BC[B[C[i] - 1] - 1] += 1

memo = [0 for i in range(n)]
for i in range(n):
    memo[A[i] - 1] += 1
ans = 0
for i in range(n):
    ans += memo[i] * BC[i]


print(ans)


