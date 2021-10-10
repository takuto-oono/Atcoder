N, K = map(int,input().split())
H = []
for i in range(N):
    h = int(input())
    H.append(h)
A = []
H = sorted(H)
for i in range(N - K + 1):
    x = H[i + K - 1] - H[i]
    A.append(x)

A = sorted(A)
ans = A[0]
print(ans) 


