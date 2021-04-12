S = input()
N = len(S)
x = 0
M = int((N - 1) / 2)
L = int((N + 3) / 2 - 1)

if S != S[ : :-1]:
    x += 1

if S[ :M] != S[ :M:-1]:
    x += 1

if S[L:N] != S[L:N:-1]:
    x += 1

if x == 0:
    print('Yes')
else:
    print('No')



    
