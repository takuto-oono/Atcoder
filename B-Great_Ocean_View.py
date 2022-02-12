n = int(input())
H = list(map(int, input().split()))
ans = 0

for i in range(n):
    if i == 0:
        ans += 1
    else:
        if H[i] >= max(H[:i]):
            ans += 1
print(ans)
