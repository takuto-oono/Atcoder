N = int(input())
X = list(map(int,input().split()))
ans_m = 0
ans_u = 0
ans_t = 0
import math
for i in range(N):
    ans_m += abs(X[i])
    ans_u += X[i] ** 2
    X[i] = abs(X[i])
    

print(ans_m)
ans_u = math.sqrt(ans_u)
print(ans_u)
ans_t = max(X)
print(ans_t)