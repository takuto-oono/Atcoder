n = int(input())
a = list(map(int,input().split()))
import collections
count = collections.Counter(a)
for i in range(n):
    y = (i + 1)
    print(y)
