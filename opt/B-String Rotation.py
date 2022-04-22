S = input()
T = input()
N = len(S)
x = 0
if S == T:
    print('Yes')
    exit()
while S != T:
    if x > N:
        print('No')
        exit()
    else:
        S = S[N - 1] + S
        S = S[0:N]
        x += 1
        if S == T:
            print('Yes')
            exit()