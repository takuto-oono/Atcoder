import collections
n = int(input())
S = input()
S = list(S)
Co = list(collections.Counter(S).values())
ans = 1

for i in range(len(Co)):
    ans *= int(Co[i]) + 1
ans -= 1
ans %= 10 ** 9 + 7
print(ans)



