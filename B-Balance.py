N = int(input())
W = list(map(int,input().split()))
x = 0
A = []
S = sum(W)
for i in range(N):
    x += W[i]
    A.append(x)
ans = S
for i in range(len(A)):
    y = S - A[i]
    z = abs(A[i] - y)
    if z < ans:
        ans = z

print(ans)