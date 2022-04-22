n, m = map(int,input().split())
AB = []
for i in range(n):
    ab = list(map(int,input().split()))
    AB.append(ab)

AB.sort()
ans = 0
for i in range(n):
    if m <= AB[i][1]:
        ans += m * AB[i][0]
        print(ans)
        exit()
    else:
        m -= AB[i][1]
        ans += AB[i][1] * AB[i][0]

print(ans)
