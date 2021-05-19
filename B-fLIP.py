n, m, k = map(int, input().split())

for i in range(n + 1):
    for j in range(m + 1):
        blacks = i * m + j * n - i * j * 2

        if blacks == k:
            print('Yes')
            exit()
print('No')
