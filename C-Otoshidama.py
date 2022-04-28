N, Y = map(int,input().split())

for i in range(N + 1):
    S = 0
    a = 10000 * i
    for j in range(N + 1):
        b = 5000 * j
        k = N - i - j
        if (Y - a - b) == 1000 * k:
            if k >= 0:
                print(i, j, k)
            
                exit()        

print('-1 -1 -1')
