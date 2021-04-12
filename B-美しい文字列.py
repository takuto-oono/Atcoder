w = input()
w = list(w)
import collections
co = collections.Counter(w)
li = co.values()
for i in li:
    if i % 2 == 1:
        print('No')
        exit()
print('Yes')
