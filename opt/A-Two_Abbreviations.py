import math
n, m = map(int,input().split())
S = input()
T = input()
if n == 1 and m == 1 and S[0] != T[0]:
    print(-1)
    exit()
ans = n * m // math.gcd(n, m)

x = ans // n
y = ans // m

for i in range(n):
    z = x * i + 1
    
    if z % y == 1:
        
        if S[i] != T[(z - 1) // y]:
            print(-1)
            exit()

print(ans)