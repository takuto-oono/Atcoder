N, D = map(int,input().split())
A = []
for i in range(N):
    XY = list(map(int,input().split()))
    A.append(XY)
B =[]
for i in A:
    x = i[0] ** 2 + i[1] ** 2
    B.append(x)
ans = 0

for i in B:
    if i <= D ** 2:
        ans += 1

print(ans)

