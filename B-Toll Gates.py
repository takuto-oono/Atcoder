N, M, X = map(int,input().split())
A = list(map(int,input().split()))
ans = []
z = 0
y = 0
for i in range(X + 1, N + 1):
    if  i in A:
        z += 1
ans.append(z)
for i in range(1,X):
    if  i in A:
        y += 1
ans.append(y)
ans = sorted(ans)
print(ans[0])