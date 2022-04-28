a, b, c, d= map(int,input().split())
import math
ans = 0
R = b - a + 1
cd = c * d // math.gcd(c, d)

ac = a // c
ad = a // d

bc = b // c
bd = b // d

if a % c == 0:
    ac -= 1
if a % d == 0:
    ad -= 1
acd = a // cd
bcd = b // cd

if a % cd == 0:
    acd -= 1

ans = R - ((bc - ac) + (bd - ad) - (bcd - acd))
print(ans)