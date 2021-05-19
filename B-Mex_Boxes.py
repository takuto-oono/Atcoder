n, k = map(int, input().split())
A = list(map(int, input().split()))
B = [0 for i in range(max(A) + 1)]


for i in range(n):
    B[A[i]] += 1
ans = 0
memo = B[0]
for i in range(len(B)):
    if memo > B[i]:
        ans += (memo - B[i]) * i
        memo = B[i]

    if i == len(B) - 1:
        ans += memo * (max(A) + 1)
print(ans)





