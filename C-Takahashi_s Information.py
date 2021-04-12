C = []
for i in range(3):
    c = list(map(int,input().split()))
    C.append(c)

for i in range(1, 3):
    x = C[i][0] - C[i - 1][0]
    y = C[i][1] - C[i - 1][1]
    z = C[i][2] - C[i - 1][2]
    if x == y and y == z:
        continue
    else:
        print('No')
        exit()
    
for i in range(1, 3):
    x = C[0][i] - C[0][i - 1]
    y = C[1][i] - C[1][i - 1]
    z = C[2][i] - C[2][i - 1]
    if x == y and y == z:
        continue
    else:
        print('No')
        exit()
    
print('Yes')