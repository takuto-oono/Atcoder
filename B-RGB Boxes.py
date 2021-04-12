R, G, B, N = map(int,input().split())
ans = 0
r = N // R + 2
g = N // G + 2
b = N // B + 2

for i in range(r):
    for j in range(g):
        x = N - i * R - j * G
        if x < 0:
            break
        if x % B == 0:
            ans += 1
print(ans)