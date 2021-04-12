n = int(input())
ans = 0
for i in range(1, 10 ** 7 + 1):
    x = i
    x = str(x)
    x_l = len(x)
    x = int(x)
    y = 10 ** x_l * x + x
    if y <= n:
        ans += 1
print(ans)
