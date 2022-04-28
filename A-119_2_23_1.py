n = int(input())
b = 0
ans = 10 ** 18
while(2 ** b <= n):
    a = n // (2 ** b)
    c = n % (2 ** b)
    ans = min(a + b + c, ans)
    b += 1

print(ans)
