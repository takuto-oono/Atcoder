n, m = map(int, input().split())
A = []
B = []

for i in range(n):
    a = input()
    A.append(a)
for i in range(m):
    b = input()
    B.append(b)

for i in range(n - m + 1):
    for j in range(n - m + 1):
        x = 0
        while (x < m):
            if A[x + i][j:j + m] == B[x]:

                x += 1
            else:
                break

        if x == m:
            print('Yes')
            exit()

print('No')

