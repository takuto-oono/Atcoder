s = int(input())
x = []
x.append(s)
m = 1
z = 0
if s % 2 == 0:
    y = s // 2
else:
    y = 3 * s + 1
m += 1
x.append(y)
while z == 0:
    n = y
    if  n % 2 == 0:
        y = n // 2
    else:
        y = 3 * n + 1
    if y in x:
        z += 1
        m += 1
        print(m)
    else:
        m += 1
        x.append(y)





