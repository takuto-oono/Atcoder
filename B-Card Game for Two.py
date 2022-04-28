N = int(input())
a = list(map(int,input().split()))
ans = 0
a = sorted(a)
a = a[::-1]
for i in range(N):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans -=a[i]
print(ans)