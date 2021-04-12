n = int(input())
A = list(map(int, input().split()))
B =[A[0]]
for i in range(n):
    if i == n - 1:
        B.append(0 - A[i])
    else:
        B.append(A[i + 1] - A[i])

C = [abs(i) for i in B]
C_sum = sum(C)

for i in range(n):
    if B[i + 1] == abs(B[i + 1]) and B[i] == abs(B[i]):
        ans = C_sum
    else:
        ans = C_sum - C[i] - C[i + 1] + abs(B[i + 1] + B[i])

    print(ans)
