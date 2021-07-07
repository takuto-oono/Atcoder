n, k = map(int, input().split())
A = list(map(int, input().split()))
D = []

x = k // n
for i in range(n):
    D.append([A[i], x])
D = sorted(D)
y = k % n
for i in range(y):
    D[i][1] += 1

for i in range(n):
    for j in range(n):
        if A[i] == D[j][0]:
            print(D[j][1])

























