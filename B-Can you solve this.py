N, M, C = map(int,input().split())
B = list(map(int,input().split()))
ans = 0
x = C


for i in range(N):
    A = list(map(int,input().split()))
    for k in range(M):
        x += A[k] * B[k]
    if x > 0:
        ans += 1
    x = C 

print(ans)
