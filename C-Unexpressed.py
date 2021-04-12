import math
n = int(input())
memo = [0]
n_sqrt = int(math.sqrt(n)) + 1
for i in range(2, n_sqrt):
    x = i
    while(x * i <= n):
        x *= i
        memo.append(x)
    
memo = set(memo)
memo = list(memo)

ans = n - len(memo) + 1

print(ans)




