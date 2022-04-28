import math
n, p = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(n):
    A[i] %= 2

count_0 = 0
count_1 = 0

for i in A:
    if i == 0:
        count_0 += 1
    else:
        count_1 += 1

if p == 0:
    x = 2 ** count_0
    y = 1
    z = 1
    while((2 * z) <= count_1):
        y += math.factorial(count_1) // (math.factorial(count_1 - 2 * z) * math.factorial(2 * z))
        z += 1

    if x == 1 and y == 0:
        ans = 0
    else:
        ans = x * y

else:
    x = 2 ** count_0
    y = 0
    z = 1
    while(2 * z - 1 <= count_1):
        y += math.factorial(count_1) // (math.factorial(count_1 - 2 * z + 1) * math.factorial(2 * z - 1))
        z += 1

    if y == 0:
        ans = 0
    else:
        ans = x * y


print(ans)





