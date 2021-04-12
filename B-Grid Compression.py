H, W = map(int,input().split())
A = []
for i in range(H):
    a = input()
    a = list(a)
    
    A.append(a)
print(A[3][3])
x = 0
y = 0
co = 0
ans_H = []
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            x += 1
        else:
            y += 1
        
    if x == W or y == W:
        ans_H.append(i)
        co += 1

        
    x = 0
    y = 0
H -= co
for i in ans_H:
    del A[i]


ans_W = []
for j in range(W):
    for i in range(H):
        if A[i][j] == '#':
            x += 1
        else:
            y += 1
        
    if x == H or y == H:
        
        ans_W.append(j)
    x = 0
    y = 0

for j in ans_W:
    for i in range(H):
        del A[i][j]
        



print(A)

            

        