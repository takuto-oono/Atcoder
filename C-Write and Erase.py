import collections
N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append(a)

ans = 0

B = collections.Counter(A)
C = B.values()
C = list(C)
for i in C:
    if i % 2 == 1:
        ans += 1
print(ans)