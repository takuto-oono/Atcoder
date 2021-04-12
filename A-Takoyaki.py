N, X, T = map(int,input().split())
import math

ans = math.ceil(N / X) * T
print(ans)