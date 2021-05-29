n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append([x, i])
    Y.append([y, i])

X = sorted(X)
Y = sorted(Y)



condidates = [[X[n - 1][0] - X[0][0], X[n - 1][1], X[0][1]],
              [X[n - 1][0] - X[1][0], X[n - 1][1], X[1][1]],
              [X[n - 2][0] - X[0][0], X[n - 2][1], X[0][1]],
              [X[n - 2][0] - X[1][0], X[n - 2][1], X[1][1]],
              [Y[n - 1][0] - Y[0][0], Y[n - 1][1], Y[0][1]],
              [Y[n - 1][0] - Y[1][0], Y[n - 1][1], Y[1][1]],
              [Y[n - 2][0] - Y[0][0], Y[n - 2][1], Y[0][1]],
              [Y[n - 2][0] - Y[1][0], Y[n - 2][1], Y[1][1]]]
condidates = sorted(condidates)
x = -1
y = -1
for i in range(len(condidates)):
    z = len(condidates) - 1 - i
    if i == 0:
        x = condidates[z][1]
        y = condidates[z][2]
    else:
        if x != condidates[z][1] or y != condidates[z][2]:
            ans = condidates[z][0]
            print(ans)
            exit()


