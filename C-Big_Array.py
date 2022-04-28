n, k = map(int, input().split())
ans = 0
memo = 0
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b])

data = sorted(data)

for i in range(n):
    memo += data[i][1]
    if memo >= k:
        ans = data[i][0]
        break
print(ans)




