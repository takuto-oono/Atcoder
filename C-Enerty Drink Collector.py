N, M = map(int,input().split())
X = []
Y = []
for i in range(N):
    X = list(map(int,input().split()))
    Y.append(X)

Y = sorted(Y)
ans = 0
for i in range(N):
    if M >= Y[i][1]:
        ans += Y[i][0] * Y[i][1]
        M -= Y[i][1]

    else:
        ans += M * Y[i][0]
        print(int(ans))
        exit()

