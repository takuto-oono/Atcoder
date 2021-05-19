def fibo(n):
    if n == 1:
        return 0
    else:
        return fibo(n - 1) + n
mod = 1000000007
n, m = map(int, input().split())
A = [1 for i in range(n + 1)]
for i in range(m):
    a = int(input())
    A[a] = 0
memo = 0
ans = 1
print(A)
for i in range(n + 1):
    if i == n:
        ans *= fibo(memo)
        print(i, fibo(memo))
    elif A[i] == 1:
        memo += 1
    else:
        if memo == 0:
            ans = 0
            break
        elif memo == 1:
            memo = 0
        else:
            ans *= fibo(memo - 1)
            print(i, fibo(memo - 1))
            memo = 0

    if ans % mod != 0:
        ans %= mod


ans %= mod


print(ans)






