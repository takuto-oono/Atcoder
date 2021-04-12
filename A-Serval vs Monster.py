h, a = map(int,input().split())
x = 0
while h > 0:
    h -= a
    x += 1

print(x)