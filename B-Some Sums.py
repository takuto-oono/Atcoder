N, A, B = map(int,input().split())

x = 0
ans = 0
for i in range(N + 1):
    i = str(i)
    l = len(i)
    for j in range(l):
        x += int(i[j])
    if A <= x <= B:
        ans += int(i)
    x = 0
print(ans)
