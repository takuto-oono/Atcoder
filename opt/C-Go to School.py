N = int(input())
A = list(map(int,input().split()))
ans = [i for i in range(N)]

for i in range(N):
    ans[A[i] - 1] = i + 1
print(*ans)
