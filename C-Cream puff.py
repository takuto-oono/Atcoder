import math
N = int(input())
x = int(math.sqrt(N)) + 1
ans = []
for i in range(1, x + 1):
    if N % i == 0:
        ans.append(i)
        y = N // i
        ans.append(y)

ans = set(ans)
ans = list(ans)
ans = sorted(ans)
l = len(ans)
for i in range(l):
    print(ans[i])




