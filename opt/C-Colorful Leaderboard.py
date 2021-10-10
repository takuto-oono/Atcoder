N = int(input())
A = list(map(int,input().split()))
mi, ma = 0, 0
co = [0, 0, 0, 0, 0, 0, 0 ,0]
z = 0

for i in A:
    if i < 3200:
        if 1 <= i < 400:
            co[0] += 1
        elif 400 <= i < 800:
            co[1] += 1
        elif 800 <= i < 1200:
            co[2] += 1
        elif 1200 <= i < 1600:
            co[3] += 1
        elif 1600 <= i < 2000:
            co[4] += 1
        elif 2000 <= i < 2400:
            co[5] += 1
        elif 2400 <= i < 2800:
            co[6] += 1
        elif 2800 <= i < 3200:
            co[7] += 1
        
    else:
        z += 1
for i in co:
    if i != 0:
        mi += 1

if mi != 0:
    ma = mi + z
else:
    mi = 1
    ma += z


if ma > 8:
    ma = 8

print(mi, ma)
