
a, b = map(int, input().split())
ans = 0
for i in range(1, b + 1):
    x = 0
    y = 0
    if a % i == 0:
        x = a
    else:
        x = (a // i) * i + i

    if b % i == 0:
        y = b
    else:
        y = (b // i) * i

    if a <= x <= b and a <= y <= b and x < y:
        ans = i


print(ans)









