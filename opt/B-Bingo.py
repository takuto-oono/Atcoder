A = []
a1 = []
a2 = []
a3 = []
for i in range(3):
    a = list(map(int,input().split()))
    for K in range(3):
        A.append(a[K])


N = int(input())
for i in range(N):
    b = int(input())
    for k in range(9):
        if b == A[k]:
            A[k] = 0




for i in range(9):
    if 0 <= i <= 2:
        a1.append(A[i])
    elif 3 <= i <= 5:
        a2.append(A[i])
    else:
        a3.append(A[i])

x = 0
y = 0
z = 0
for i in range(3):
    if a1[i] == 0:
        x += 1
    if a2[i] == 0:
        y += 1
    if a3[i] == 0:
        z += 1

if x == 3 or y == 3 or z == 3:
    print('Yes')
    exit()

for i in range(3):
    if a1[i] == 0 and a2[i] == 0 and a3[i] == 0:
        print('Yes')
        exit()

if a2[1] == 0:
    if a1[0] == 0 and a3[2] == 0 or a1[2] == 0 and a3[0] == 0:
        print('Yes')
        exit()

print('No')




