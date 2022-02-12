n, k = map(int,input().split())
h = list(map(int,input().split()))
x = 0

for i in range(n):
    if h[i] >= k:
        x += 1

print(x)
