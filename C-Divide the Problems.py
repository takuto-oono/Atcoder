N = int(input())
d = list(map(int,input().split()))
d = sorted(d)
ans = 0
if d[N // 2 - 1] == d[N // 2]:
    print(0)
    exit()
ans = d[N // 2] - d[N // 2 - 1] 
print(ans)