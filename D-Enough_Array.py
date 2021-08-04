n, k = map(int, input().split())
A = list(map(int, input().split()))

def check(i, k):
    ok = n + 1
    ng = -1

    while(ok - ng > 1):
        mid = (ok + ng // 2)
        x = sum(A[i:mid])
        if x >= k:
            ok = mid
        else:
            ng = mid
    return n - ok + 1

ans = 0
for i in range(n):
    ans += check(i, k)

print(ans)


