S = input()
N = len(S)
a = []
for i in range(N):
    if S[i] in a:
        print('no')
        exit()
    else:
        a.append(S[i])
print('yes')
