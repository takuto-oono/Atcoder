t = int(input())
C = []
Ans = []
for i in range(t):
    n = int(input())
    C = list(map(int, input().split()))
    memok = 0
    memog = 1
    j = 1
    ans = []
    C_ans = sorted(C)
    while(j <= n ** 2):
        if j % 2 == 0:
            if memog < n - 1:
                if C[memog] > C[memog + 1]:
                    C[memog], C[memog + 1] = C[memog + 1], C[memog]
                    ans.append(str(memog + 1))
                    j += 1
                else:
                    memog += 2
            else:
                memog = 1
        else:
            if memok < n - 1:
                if C[memok] > C[memok + 1]:
                    C[memok], C[memok + 1] = C[memok + 1], C[memok]
                    j += 1
                    ans.append(str(memok + 1))
                else:
                    memok += 2
            else:
                memok = 0

        if C == C_ans:
            Ans.append(ans)
            break

for i in range(t):

    ans = Ans[i]
    if len(ans) == 0:
        print(0)
    else:
        print(' '.join(ans))



