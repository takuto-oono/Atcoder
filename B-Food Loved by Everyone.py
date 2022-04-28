N, M = map(int,input().split())
a = []
ans = range(1,M + 1)
ans = list(ans)
for i in range(N):
    A = list(map(int,input().split()))
    K = A[0]
    A.remove(A[0])
    for j in range(1,M + 1):
        if j not in A:
            a.append(j)
for i in a:
    if i in ans:
        ans.remove(i)
print(len(ans))


        
