N = int(input())
A = list(map(int,input().split()))
ans = 2
y = 0
z = 0
x = max(A)
for i in range(2, x + 1):
    for j in range(N):
        if A[j] % i == 0:
            y += 1
    
    if z < y:
        ans = i
        z = y
    
    y = 0

print(ans)



