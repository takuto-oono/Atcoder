x, n = map(int,input().split())
p = list(map(int,input().split()))
y = 0
z = 0
while y == 0:
    a = x + z
    b = x - z
    if a in p and b in p:
        z += 1
    elif a not in p and b in p:
        print(a)
        y = 4
    elif b not in p:
        print(b)
        y = 5





