N = int(input())
TXY = []
txy = []
for i in range(N):
    txy = list(map(int,input().split()))
    TXY.append(txy)
ans = 'Yes'

for i in range(N):
    t = TXY[i][0]
    x = TXY[i][1]
    y = TXY[i][2]
    if i == 0:
        dis = x + y
        if dis > t:
            ans = 'No'
            break
        else:
            if (dis - t) % 2 == 1:
                ans = 'No'
                break

    else:
        tb = TXY[i - 1][0]
        xb = TXY[i - 1][1]
        yb = TXY[i - 1][2]
        t -= tb
        x = abs(x - xb)
        y = abs(y - yb)
        dis = x + y
        if dis > t:
            ans = 'No'
            break
        else:
            if (dis - t) % 2 == 1:
                ans = 'No'
                break
print(ans)