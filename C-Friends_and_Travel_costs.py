n, k = map(int, input().split())
AB = []
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    AB.append([a, b])

AB = sorted(AB)


for i in range(n):
    if i == n - 1:
        if k < AB[i][0]:
            ans = k
            break
        else:
            k += AB[i][1]
            if k > 10 ** 100:
                k = 10 ** 100
            ans = k
    else:
        if k < AB[i][0]:
            ans = k
            break
        else:
            ans = AB[i][0]
            k += AB[i][1]

print(ans)

