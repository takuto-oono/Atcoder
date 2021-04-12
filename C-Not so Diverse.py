N, K = map(int,input().split())
A = list(map(int,input().split()))
B = [0] * N

for i in range(N):
    B[A[i] - 1] += 1

C = sorted(B)
x = 0
y = 0
for i in range(N):
    x += C[-i - 1]
    y += 1

    if y >= K:
        break

ans = N - x
print(ans)
