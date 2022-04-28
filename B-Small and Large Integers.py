A, B, K = map(int,input().split())
ans = []
for i in range(K):
    if A + i <= B:
        ans.append(A + i)
for i in range(-K,0):
    if B + i >= A:
        ans.append(B + i + 1)
ans = list(set(ans))
ans = sorted(ans)
for i in range (len(ans)):
    print(ans[i])


    