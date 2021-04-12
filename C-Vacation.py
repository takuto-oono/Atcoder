n = int(input())
ABC = []
for i in range(n):
    abc = list(map(int,input().split()))
    ABC.append(abc)
dp_last_a = [0 for i in range(n + 1)]
dp_last_b = [0 for i in range(n + 1)]
dp_last_c = [0 for i in range(n + 1)]

for i in range(n):
    dp_last_a[i + 1] = max(dp_last_b[i] + ABC[i][0], dp_last_c[i] + ABC[i][0])
    dp_last_b[i + 1] = max(dp_last_a[i] + ABC[i][1], dp_last_c[i] + ABC[i][1])
    dp_last_c[i + 1] = max(dp_last_a[i] + ABC[i][2], dp_last_b[i] + ABC[i][2])

ans = max(dp_last_a[n], dp_last_b[n], dp_last_c[n])
print(ans)


