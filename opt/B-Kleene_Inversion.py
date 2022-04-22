n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    memo1 = 0
    memo2 = 0
    for j in range(n):
        if j < i and A[j] > A[i]:
            memo1 += 1
        if j > i and A[j] > A[i]:
            memo2 += 1
    ans += k * memo1
    memo = memo1 + memo2
    ans += (memo + memo * (k - 1)) * (k - 1) // 2
    ans %= 10 ** 9 + 7
print(ans)
