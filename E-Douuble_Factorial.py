n = int(input())
ans = 0
x = 10
if n % 2 == 0:
    while(n >= x):
        ans += n // x
        x *= 5


print(ans)
