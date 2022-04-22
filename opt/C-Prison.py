N, K, Q = map(int,input().split())
a = []
for i in range(Q):
    A = int(input())
    a.append(A)
if K > Q:
    for i in range(N):
        print('Yes')
for i in range(1,N + 1):
    if Q - K + 1 <= a.count(i):
        print('Yes')
    else:
        print('No')
