K = int(input())
ans = 1
x = 1
z = 0

if K % 2 == 0:
    print('-1')
else:
    while z == 0:
        y = K * x
        if y % 11 == 0 and y % 7 == 0:
            y = str(y)
            print(len(y))
            z += 1
        elif y == 7:
            print(1)
        else:
            x += 1
            




