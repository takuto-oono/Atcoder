n = int(input())
z= 0

for x in range(1,10):
    for y in range(1,10):
        if n == x * y:
            z += 1

if z == 0:
    print('No')
else:
    print('Yes')