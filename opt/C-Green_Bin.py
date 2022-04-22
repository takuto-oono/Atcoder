n = int(input())
S = []

for i in range(n):
    s = input()
    s = list(s)
    s = sorted(s)
    S.append(s)

S = sorted(S)

ans = 0
memo = 1
for i in range(n - 1):
    if i == n - 2:
        if S[i] == S[i + 1]:
            memo += 1
        ans += memo * (memo - 1) // 2
    else:
        if S[i] == S[i + 1]:
            memo += 1
        else:
            ans += memo * (memo - 1) // 2
            memo = 1

print(ans)