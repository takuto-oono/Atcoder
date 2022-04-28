a, b, c, d = map(int, input().split())
x = a / (c * d - b)
ans = 0
import math

if x > 0:
    ans = math.ceil(x)
elif x <= 0:
    ans = -1
print(ans)


