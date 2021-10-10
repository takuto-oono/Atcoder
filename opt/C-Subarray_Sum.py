n, k, s = map(int, input().split())
if k == 0:
    if s == 10 ** 9:
        print(' '.join([str('3') for i in range(n)]))
    else:
        print(' '.join([str(s + 1) for i in range(n)]))
    exit()
x = 1
if n - k >= s:
    while(k % x == 0):
        x += 1

Ans = [str(s) for i in range(k)] + [str(x) for j in range(n - k)]

print(' '.join(Ans))

