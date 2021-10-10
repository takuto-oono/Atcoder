N = int(input())
ans = [2, 1]
for i in range(2, N + 1):
    x = ans[i-2] + ans[i-1]
    ans.append(x)

print(ans[N])