N = int(input())
a = []
ans = []
for i in range(N):
    A = int(input())
    a.append(A)

b = sorted(a)

m = max(a)
for i in a:
    if i == m:
        ans.append(b[-2])
    else:
        ans.append(m)

for i in ans:
    print(i)


    