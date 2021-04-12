K, N = map(int,input().split())
A = list(map(int,input().split()))
x = []

for i in range(N - 1):
    x.append(A[i + 1] - A[i])
x.append(A[0] + K - A[N - 1])
x = sorted(x)
del x[N - 1]
print(sum(x))
