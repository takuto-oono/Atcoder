n = int(input())
D = list(map(int,input().split()))
m = int(input())
T = list(map(int,input().split()))

D = sorted(D)
T = sorted(T)
j = 0
co = 0

for i in range(m):
    if j == n:
        print('NO')
        exit()
    x = 0
    while(x == 0):
        
        if T[i] < D[j]:
            print('NO')
            exit()
        elif T[i] == D[j]:
            co += 1
            x = 1
            j += 1
        elif T[i] > D[j]:
            j += 1
if co == m:
    print('YES')
else:
    print('NO')




