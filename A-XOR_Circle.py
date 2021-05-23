n = int(input())
A = list(map(int, input().split()))
memo = [0 for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if memo[i] < 2 and memo[j] < 2:

            x = A[i] ^ A[j]
            for k in range(j + 1, n):
                if A[k] == x and memo[k] < 2:
                    memo[i] += 1
                    memo[j] += 1
                    memo[k] += 1

                    break


if n == 3:

    for i in range(n):
        if memo[i] == 1:
            continue
        else:
            print('No')
            exit()
    print('Yes')
else:
    for i in range(n):
        if memo[i] == 2:
            continue
        else:
            print('No')
            exit()
    print('Yes')



