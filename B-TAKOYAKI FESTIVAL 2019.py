n = int(input())
d = list(map(int,input().split()))
z = 0

for x in range(n - 1):
    for y in range(x + 1,n):
        z += d[x] * d[y]
        

print(z)


