N, K, Q = map(int,input().split())
a = []
b = [0] * N
for i in range(Q):
    A = int(input())
    a.append(A)

for i in a:
    b[i - 1] += 1
for i in b:
    if i > Q - K:
        print('Yes')
    else:
        print('No')




