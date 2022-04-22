
X, Y = map(int,input().split())

z = 0
for a in range(X + 1):
    if Y == 4 * a + 2 * (X - a):
        z += 1

if z > 0:
    print('Yes')
else:
    print('No')