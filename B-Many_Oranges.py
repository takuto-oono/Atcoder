a, b, w = map(int,input().split())
mi = 10 ** 9
ma = 0

for i in range(10 ** 6 + 1):
    if a * i <= w * 1000 <= b * i:
        mi = min(i, mi)
        ma = max(i, ma)
    
if ma == 0:
    print('UNSATISFIABLE')
else:
    print(mi, ma)
    