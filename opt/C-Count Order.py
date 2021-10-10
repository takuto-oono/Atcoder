N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
n = range(1,N + 1)
import itertools 
l = list(itertools.permutations(n))
a = 0
b = 0
for i in l:
    if i == tuple(P):
        a += 1
        break
    else:
        a += 1
for i in l:
    if  i == tuple(Q):
        b += 1
        break
    else:
        b += 1
print(abs(a - b))