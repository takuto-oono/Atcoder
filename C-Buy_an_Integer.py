a, b, x = map(int, input().split())

ok = 0
ng = 10 ** 9 + 1

def f(x, a, b):
    return a * x + b * len(str(x))

while(ok + 1 != ng):

    y = (ok + ng) // 2
    if f(y, a, b) <= x:
        ok = y
    else:
        ng = y
print(ok)



