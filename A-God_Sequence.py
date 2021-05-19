a, b = map(int, input().split())
Ans = []
if a == b:
    Ans += [i + 1 for i in range(a)] + [-(i + 1) for i in range(a)]
elif a < b:
    x = b - a + 1
    dif = (x + 1) * x // 2
    Ans.append(dif)
    Ans += [10 ** 9 - i for i in range(a - 1)] + [-(10 ** 9 - i) for i in range(a - 1)] + [-(i + 1) for i in range(x)]
else:
    x = a - b + 1
    dif = (x + 1) * x // 2
    Ans.append(-dif)
    Ans += [10 ** 9 - i for i in range(b - 1)] + [-(10 ** 9 - i) for i in range(b - 1)] + [(i + 1) for i in range(x)]
print(*Ans)