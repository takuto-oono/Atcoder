K = int(input())

import itertools
import math
num = [i for i in range(1, K + 1)]
l = itertools.permutations(num, 3)

ans = 0
for i in l:

    ans += math.gcd(*i)
    print(i)
print(ans)
