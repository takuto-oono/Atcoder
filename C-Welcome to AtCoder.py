N, M = map(int,input().split())
yes = []
no = 0

for i in range(M):
    pS = list(input().split())
    if pS[1] == 'AC':
        if pS[0] not in yes:
            yes.append(pS[0])
    else:
        if pS[0] not in yes:
            no += 1
            

x = len(yes)

print(x, no)

print(yes)

