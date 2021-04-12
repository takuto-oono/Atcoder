import collections
n = int(input())
A = list(map(int, input().split()))
ans = 0

Count = collections.Counter(A)
keys = Count.keys()

for i in keys:
    if Count[i] < i:
        ans += Count[i]
    elif Count[i] > i:
        ans += Count[i] - i

print(ans)











