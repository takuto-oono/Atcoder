h, w = map(int, input().split())

A = []
for i in range(h):
    a = input()
    a = list(a)
    A.append(a)

i = 0
j = 0

while(i != h - 1 or j != w - 1):
    if i == h - 1:
        if A[i][j + 1] == '#':
            A[i][j] = '.'
            j += 1
            
        else:
            print('Impossible')
            exit()
    elif j == w - 1:
        if A[i + 1][j] == '#':
            A[i][j] = '.'
            i += 1
            
        else:
            print('Impossible')
            exit()
    else:
        if A[i + 1][j] == '#' and A[i][j + 1] == '#':
            print('Impossible')
            exit()
        elif A[i + 1][j] == '#':
            A[i][j] = '.'
            i += 1
            
        elif A[i][j + 1] == '#':
            A[i][j] = '.'
            j += 1
            
        else:
            print('Impossible')
            exit()
A[i][j] = '.'

for i in range(h):
    for j in range(w):
        if A[i][j] == '#':
            print('Impossible')
            exit()


print('Possible')



