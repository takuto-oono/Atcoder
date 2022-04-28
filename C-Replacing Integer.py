N, K = map(int,input().split())
N = N % K
if N - K <= 0:
    M = K - N
else:
    M = N - K
print(min(M, N))
