N = int(input())
v = list(map(int,input().split()))
v = sorted(v)
ans = (v[0] + v[1]) / 2
for i in range(2,N):
    ans = (ans + v[i]) / 2
print(ans)
    
