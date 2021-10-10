N = int(input())
p = list(map(int,input().split()))
x = 0

for i in range(N):
    if i + 1 != p[i]:
        x += 1

if x == 2 or x == 0:
    print('YES')
else:
    print('NO')