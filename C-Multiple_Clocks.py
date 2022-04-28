import math
n = int(input())
T = []


ans = 1
for i in range(n):
    t = int(input())
    ans = ans * t // math.gcd(ans, t)

print(ans)