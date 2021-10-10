S = input()
S = list(S)

T = 'keyence'
T = list(T)
N = len(S)
x = 0
y = 0

for i in range(N):
    for j in range(N):
        if S[ :i] + S[j: ] == T:
            print('YES')
            exit()
print('NO')



