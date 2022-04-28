a, b, c, d = map(int,input().split())
while a > 0:
    c -= b
    a -= d

if c <= 0:
    print('Yes')
else:
    print('No')