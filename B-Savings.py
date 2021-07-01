n = int(input())
x = 0
for i in range(1, 10 ** 9):
    x += i
    if x >= n:
        print(i)
        exit()
