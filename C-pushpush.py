n = int(input())
A = list(map(int, input().split()))
B = ['0' for i in range(n)]
if n % 2 == 0:
    for i in range(n // 2):
        B[i + n // 2] = str(A[2 * i])
        B[n // 2 - i - 1] = str(A[2 * i + 1])

else:

    for i in range(n // 2 + 1):
        if i == 0:
            B[n // 2] = str(A[i])
        else:
            B[n // 2 + i] = str(A[2 * i - 1])
            B[n // 2 - i] = str(A[2 * i])

ans = ' '.join(B)
print(ans)
