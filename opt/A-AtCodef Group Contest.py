N = int(input())
a = list(map(int,input().split()))
ans = 0
a = sorted(a)
for i in range(N):
    ans += a[-2 - 2 * i]
print(ans)