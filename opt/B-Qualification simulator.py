N, A, B = map(int,input().split())
S = input()
x = 0
y = 0
z = x + y

for i in range(N):
    if S[i] == 'a':
        if z < A + B:
            print('Yes')
            x += 1
            z = x + y
        else:
            print('No')
    elif S[i] == 'b':
        if z < A + B and y < B:
            print('Yes')
            y += 1
            z = x + y
        else:
            print('No')
    else:
        print('No')
