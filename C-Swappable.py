n = int(input())
A = list(map(int, input().split()))
ans = 0
A = sorted(A)
i = 0
while(i < n):
    memo = 1
    for j in range(i + 1, n):
        if A[j] == A[i]:
            memo += 1
        else:
            break
    ans += memo * (n - memo)
    i += memo
ans = ans // 2
print(ans)

