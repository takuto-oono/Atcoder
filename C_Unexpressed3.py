import math
n = int(input())
memo = [0]
n_sqrt = int(math.sqrt(n)) + 1

for i in range(2, n_sqrt):
    for j in range(2, 10000000):
        x = i ** j
        if x <= n:
            memo.append(x)
        else:
            break
print(memo)
memo = set(memo)
print(memo)
memo = list(memo)

ans = n - len(memo) + 1
print(ans)
