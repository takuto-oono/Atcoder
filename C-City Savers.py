N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0

for i in range(N):
    a = A[i]
    b = B[i]
    c = A[i + 1]
    if b <= a:
        ans += b
    else:
        b -= a
        ans += a
        if b < c:
            ans += b
            c -= b
            A[i + 1] = c
        else:
            A[i + 1] = 0
            ans += c

print(ans)

