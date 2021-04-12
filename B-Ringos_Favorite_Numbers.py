d, n = map(int,input().split())
if d == 0:
    if n != 100:
        print(n)
    else:
        print(101)
elif d == 1:
    if n == 100:
        print(10100)
    else:
        print(100 * n)
else:
    if n == 100:
        print(1010000)
    else:
        print(n * 100 * 100)
