import math
x = int(input())
y = 0
z = 100
while z < x:
    z = (math.floor(z * 1.01))
    y += 1
    print(z)
print(y)