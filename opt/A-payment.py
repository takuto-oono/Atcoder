N = float(input())
if int(N) % 1000 == 0:
    print(0)
else:
    M = (int(N / 1000) + 1) * 1000
    print(int(M - N))


