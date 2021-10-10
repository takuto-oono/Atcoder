S = input()

L = len(S)
if S[L - 1] == 's':
    print(S + 'es')
else:
    print(S + 's')

