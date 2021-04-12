s = input()
t = input()
S = list(s)
T = list(t)

S = sorted(S)
T = sorted(T)
T = T[ : :-1]

S = ''.join(S)
T = ''.join(T)
A = [S, T]
A = sorted(A)
if S == T:
    print('No')
    exit()

if A[0] == S:
    print('Yes')

else:
    print('No')

