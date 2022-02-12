N, D = map(int,input().split())
import math
X = [input().split() for i in range(N)]



ans = 0
a = 0

for i in range(N):
    for j in range(N):
        if i != j:
            for k in range(D):
                a += (int(X[i][k]) - int(X[j][k])) ** 2
            a = math.sqrt(a)
            if int(a) == a:
                ans += 1            
            a  = 0
print(ans // 2)