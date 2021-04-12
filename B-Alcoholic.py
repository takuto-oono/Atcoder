n, x = map(int,input().split())

alcohol = 0


for i in range(n):
    v, p = (map(int,input().split()))
    
    alcohol += v * p
    if alcohol > x * 100:
        print(i + 1)
        exit()
    
print(-1)
