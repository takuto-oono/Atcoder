import math
n, m = map(int,input().split())
a = list(map(int,input().split()))
sum = sum(a)

x = 0
for i in a:
    if i * 4 * m >= sum:
        x += 1


if x >= m:
    print('Yes')
else:
    print('No')
