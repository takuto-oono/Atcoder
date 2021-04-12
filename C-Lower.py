N = int(input())
H = list(map(int,input().split()))
a = 0
ans = [0]
for i in range(N - 1):
    if H[i + 1] <= H[i]:
        a += 1
        if i == N - 2:
            ans.append(a)
    else:
        ans.append(a)
        a = 0
ans = sorted(ans)
l = len(ans)
print(ans[l - 1])
