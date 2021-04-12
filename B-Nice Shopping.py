A, B, M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = []
for i in range(M):
    x, y, c = map(int,input().split())
    z = a[x - 1] + b[y - 1] - c
    ans.append(z)
z = min(a) + min(b)
ans.append(z)
ans = sorted(ans)
print(ans[0])