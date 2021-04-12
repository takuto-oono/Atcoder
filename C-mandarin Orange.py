n = int(input())
A = list(map(int,input().split()))
ans = 0

for i in range(n):
    A_min = A[i]
    for j in range(i,n):
        A_min = min(A_min, A[j]) 
        x = A_min * (j - i + 1)
        if x > ans:
            ans = x

print(ans)