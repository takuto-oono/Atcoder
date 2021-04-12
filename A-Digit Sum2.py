ans = 0
N = int(input())
N = str(N)
n = len(N)

a = int(N) // 10 ** (n - 1) * 10 * (n - 1) - 1
x = 0
a = str(a)
for i in range(n):
    x += int(a[i])

y = 0
b = N[0] + '0' * (n - 1)
b = int(b)
    
for i in range(b, N + 1):
    i = str(i)
    for j in range(n):
        y += i[j]
    z = max(z, y)
    y = 0

print(max(x, z))