S = input()
N = len(S)
x = 0
if S[0] == 'A':
    if S[1] == 'C' or S[-1] == 'C':
        print('WA')
    else:
        if S.count('C') == 1:
            S.replace('A', '')
            S.replace('C', '')
            N = len(S)
            for i in range(N):
                if 97 <= ord(S[i]) <= 122:
                    x += 1
            if x == N - 2:
                print('AC')
            else:
                print('WA')
        else:
            print('WA')
else:
    print('WA')




