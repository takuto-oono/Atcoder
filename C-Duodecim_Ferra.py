l = int(input())
import math
ans = 1
l -= 12
x = l
while(l > 0):
    ans *= 12
    l -= 1
ans //= math.factorial(x)
print(ans)

a,b = b, a