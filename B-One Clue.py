K, X = map(int,input().split())
ans = []
if K == 1:
    print(X)
else:
    for i in range(-K + 1,K):
        ans.append(X + i)

print(*ans)
