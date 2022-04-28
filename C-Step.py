N = int(input())
A = list(map(int,input().split()))
x = A[0]
ans = 0
for i in range(1,N):
    if A[i] < x:
        ans += x - A[i]
    elif A[i] > x:
        x = A[i]
    print(x, ans)
print(ans)