n, k = map(int,input().split())
x = 0


for i in range(0,41):
    if n % k ** i != n:
        x += 1
    else:
        x = x
print(x)
