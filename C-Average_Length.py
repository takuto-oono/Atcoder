import math
n = int(input())
XY = []
for i in range(n):
    xy = list(map(int, input().split()))
    XY.append(xy)

sum_of_dis = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        
        sum_of_dis += math.sqrt((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2)

ans = (sum_of_dis * math.factorial(n - 1)) * 2 / math.factorial(n)
print(ans)