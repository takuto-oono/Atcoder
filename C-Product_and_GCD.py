def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp %i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr
n, p = map(int, input().split())
Prime_factor = factorization(p)



co = 0
ans = 1
for i in range(len(Prime_factor)):
    if Prime_factor[i][1] >= n:
        ans *= Prime_factor[i][0] ** (Prime_factor[i][1] // n)

print(ans)



