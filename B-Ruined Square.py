x1, y1, x2, y2 = map(int,input().split())
x12 = x2 - x1
y12 = y2 - y1
x3 = x2 - y12
y3 = y2 + x12
x4 = x3 -x12
y4 = y3 -y12
print(x3, y3, x4, y4)
