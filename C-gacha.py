n = int(input())
list = []
for i in range(n):
    a = input()
    list.append(a)

import collections

x = collections.Counter(list)
y = x.keys()
print(len(y))