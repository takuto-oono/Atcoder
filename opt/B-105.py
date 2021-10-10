n = int(input())
def divisor(n):
    i = 1
    co = 0
    while(i * i <= n):
        if n % i == 0:
            if n / i == i:
               co += 1
            else:
                co += 2
        i += 1

    return co

ans = 0
for i in range(1, n + 1, 2):
    x = divisor(i)

    if x == 8:
        ans += 1

print(ans)



