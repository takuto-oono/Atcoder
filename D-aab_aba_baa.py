a, b, k = map(int, input().split())
n = a + b
import itertools
memo = [i for i in range(n)]

memo2 = itertools.permutations(memo, b)
co = 0
for m in memo2:
    co += 1
    if co == k:
        print(m)








