D, N = map(int,input().split())
z = 0
x = 1
y = 0

if D == 0:
    while z == 0:
        if x % 100 != 0:
            y += 1
            if y == N:
                print(x)
                z += 1
        x += 1
    exit()
while z == 0:
    x += 1
    if x % (100 ** D) == 0:
        z += 1
    

print(x * N)

