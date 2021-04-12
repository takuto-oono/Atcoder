N = int(input())
A = list(map(int,input().split()))
ans = 0
y = []
x = 0
z = 1
while x == 0:
    for i in range(N):
        a = str(A[i] % (2 ** z))
        y.append(a)
    if y.count('0') == N:
        ans += 1
        y = []
        z += 1
    else:
        x =+ 3
print(ans)
