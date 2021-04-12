n, m = map(int, input().split())
Half_Point_1 = []
Half_Point_2 = []
for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        Half_Point_1.append(b)

    elif b == n:
        Half_Point_2.append(a)


Half_Point_1 = set(Half_Point_1)
Half_Point_2 = set(Half_Point_2)

l_1 = len(Half_Point_1)
l_2 = len(Half_Point_2)
X = Half_Point_2 & Half_Point_1
X = list(X)
if len(X) > 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')






