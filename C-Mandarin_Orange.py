n = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(n):
    x = A[i]
    for j in range(i, n):
        if x > A[j]:
            x = A[j]
        condidate = x * (j - i + 1)
        
        if condidate > ans:
            ans = condidate
        

print(ans)


