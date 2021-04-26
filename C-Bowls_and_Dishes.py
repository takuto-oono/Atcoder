n, m = map(int, input().split())
AB = []
for i in range(m):
    a, b = map(int, input().split())
    AB.append([a, b])
k = int(input())
CD = []
check_list = [-10 ** 10 for i in range(n)]
for i in range(k):
    c, d = map(int, input().split())
    CD.append([c, d])
    check_list[c - 1] = 1
    check_list[d - 1] = 1

value_list = [0 for i in range(n)]

for i in range(m):
    for j in range(2):
        value_list[AB[i][j] - 1] += 1

for i in range(k):
    for j in range(2):
        value_list[CD[i][j] - 1] -= 1

for i in range(k):
    x = CD[i][0]
    y = CD[i][1]
    if check_list[x - 1] == 1 and check_list[y - 1] == 1:
        if value_list[x - 1] <= value_list[y - 1]:
            check_list[y - 1] = 0
            value_list[x - 1] += 1
        else:
            check_list[x - 1] = 0
            value_list[y - 1] += 1
    elif check_list[x - 1] == 1:
        check_list[x - 1] = 0


    elif check_list[y - 1] == 1:
        check_list[y - 1] = 0

ans = 0
for i in range(m):
    x = AB[i][0]
    y = AB[i][1]
    if check_list[x - 1] == 0 and check_list[y - 1] == 0:
        ans += 1
print(ans)
