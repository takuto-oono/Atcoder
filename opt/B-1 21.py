a, b = input().split()
x = int(a + b)
for i in range(x // 2 + 1):
    if i * i == x:
        print('Yes')
        exit()

print('No')  