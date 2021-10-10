N, x = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
ans = 0
for i in range(len(a) - 1):
    x -= a[i]
    if x >= 0:
        ans += 1
    else:
        break
x -= a[N - 1]
if x == 0:
    ans += 1
print(ans)