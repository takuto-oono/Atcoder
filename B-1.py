X = int(input())
x = 100
ans = 0
import math

while x + 1 < X:
    x *= 1.01
    y = x
    y = math.floor(y)
    ans += 1
    if y == X:
        print(ans)
        exit()
