n = int(input())

memo = [1 for i in range(10 ** 4)]

s = 0
for i in range(1, (10 ** 4) + 1):
    s += i



for i in range(1, (10 ** 4) + 1):
    x = (10 ** 4) - i + 1
    if s - x >= n:
        s -= x
        memo[x - 1] = 0
    if s == n:
        break


for i in range(10 ** 4):
    if memo[i] == 1:
        print(i + 1)



