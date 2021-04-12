import math
n, m = map(int,input().split())
S = input()
T = input()
ans = n * m // math.gcd(n, m)
Condidate = ['0' for i in range(ans)]
x = ans // n
y = ans // m
for i in range(min(n, m)):
    a = x * i + 1
    b = y * i + 1
    if Condidate[a - 1] == '0' or Condidate[a - 1] == S[i]:
        Condidate[a - 1] = S[i]

    else:
        ans = -1
        break

    if Condidate[b - 1] == '0' or Condidate[b - 1] == T[i]:
        Condidate[b - 1] = T[i]

    else:
        ans = -1
        break
print(ans)

