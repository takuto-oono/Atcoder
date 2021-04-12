A,B = map(int,input().split())
a = 0
ans = 0
for i in range(A, B + 1):
    i = str(i)
    l = len(i)
    for j in range(l):
        if i[0 + j] == i[l - j - 1]:
            a += 1
    if a == l:
        ans += 1
    a = 0
print(ans)