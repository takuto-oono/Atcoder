n, m = map(int, input().split())
memo = [1] + [0 for i in range(n - 1)]
memo2 =[1 for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    if memo[x - 1] == 1 and memo2[x - 1] == 1:
        memo[x - 1] = 0
        memo[y - 1] = 1
        memo2[x - 1] -= 1
        memo2[y - 1] += 1

    elif memo[x - 1] == 1 and memo2[x - 1] >= 2:
        memo[y - 1] = 1
        memo2[x - 1] -= 1
        memo2[y - 1] += 1

    elif memo[x - 1] == 0:
        memo2[x - 1] -= 1
        memo2[y - 1] += 1




ans = 0
for i in range(n):
    if memo[i] >= 1:
        ans += 1

print(ans)


