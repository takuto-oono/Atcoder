N = int(input())
a = int(N / 10)
x = 0

for i in range(a,N + 1):
    if N == int(i * 1.08):
        print(i)
        x += 1

if x == 0:
    print(':(')