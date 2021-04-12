n = int(input())
xyz = []
for i in range(n):
    xy = list(map(int,input().split()))
    xyz.append(xy)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        z = (xyz[i][1] - xyz[j][1]) / (xyz[i][0] - xyz[j][0])
        if -1 <= z <= 1:
            ans += 1

print(ans)

