N = input()

n = len(N)
x = 0
for i in range(n):
    x += int(N[i])

if x % 9 == 0:
    print('Yes')
else:
    print('No')