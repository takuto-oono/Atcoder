A, B = map(int,input().split())
mi = 10 * B - 1
x = 0
ma = 15 * B + 1


while x == 0:
    if int(mi * 0.08) == A and int(mi * 0.1) == B:
        x = 1
    elif mi == ma:
        x = 1
        mi = -1
    else:
        mi += 1
print(mi)