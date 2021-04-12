N = int(input())
a = list(map(int,input().split()))
ans = 0
x = 0

while x <= N - 1:
    if ans + 1 == a[x]:
        ans += 1
    x += 1
    
if ans == 0:
    print(-1)
else:
    print(N - ans)

