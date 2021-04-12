N, M = map(int,input().split())
a = []
b = []
for i in range(M):
    L, R = map(int,input().split())
    a.append(L)
    b.append(R)
a = sorted(a)
b = sorted(b)
A = a[M - 1]
B = b[0]
if A <= B:
    print(B - A + 1)
else:
    print(0)