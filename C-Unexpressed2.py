import math
n = int(input())
n_sqrt = int(math.sqrt(n)) + 1
memo = [i for i in range(1, n + 1)]


for i in range(2, n_sqrt):
    x = i
    while(x * i <= n):
        x *= i
        memo[x - 1] = 0

ans = 0
for i in range(len(memo)):
    if memo[i] != 0:
        ans += 1

print(ans)





