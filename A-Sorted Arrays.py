N = int(input())
A = list(map(int,input().split()))
x = 0
ans = 0
y = 0
z = 0
for i in range(N - 1):
    x = A[i + 1] - A[i]
    if x > 0:
        if z > 0:
            z = 0
            ans += 1
        
        elif y >= 0:
            y += 1

    elif x < 0:
        if y > 0:
            y = 0
            ans += 1

        elif z >= 0:
            z += 1
    

print(ans + 1)