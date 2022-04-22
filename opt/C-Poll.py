N = int(input())
import collections
a = []

for i in range(N):
    S = input()
    a.append(S)

l = collections.Counter(a)

x = max(l.values())

ans = [k for k, v in l.items() if v == x]
ans = sorted(ans)


for i in ans:
    print(i)




