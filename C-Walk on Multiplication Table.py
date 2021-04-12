N = int(input())
import math
y = int(math.sqrt(N))
ans = 10 ** 12

for i in range(1,y + 2):
    if N % i == 0:
        x = N // i + i - 2
        ans = min(ans,x)

print(ans)

