N = int(input())
A = []
for i in range(N):
    W = input()
    A.append(W)
for i in A:
    if A.count(i) != 1:
        print('No')
        exit()
for i in range(N - 1):
    if A[i][-1] != A[i + 1][0]:
        print('No')
        exit()
print('Yes')

