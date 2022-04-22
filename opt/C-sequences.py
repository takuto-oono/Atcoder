n = int(input())
V = list(map(int, input().split()))

V1 = [V[i] for i in range(0, n, 2)]
V2 = [V[i] for i in range(1, n, 2)]

memo1 = [[0, i + 1] for i in range(10 ** 5)]
memo2 = [[0, i + 1] for i in range(10 ** 5)]

for i in range(len(V1)):
    memo1[V1[i] - 1][0] += 1
    memo2[V2[i] - 1][0] += 1

memo1 = sorted(memo1)
memo2 = sorted(memo2)

ans = 0
l = len(memo2)

if memo1[l - 1][1] == memo2[l - 1][1]:
    ans = min(n - memo1[l - 2][0] - memo2[l - 1][0], n - memo1[l - 1][0] - memo2[l - 2][0])
else:
    ans = n - memo1[l - 1][0] - memo2[l - 1][0]

print(ans)
