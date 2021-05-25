S = input()
n = len(S)
memo = [0 for i in range(26)]

for i in range(n):
    x = ord(S[i]) - 97
    memo[x] += 1

print(memo)
ans = 0
while (max(memo) != len(S)):
    ans += 1
    S_new = ''
    for i in range(len(S) - 1):
        x = ord(S[i]) - 97
        y = ord(S[i + 1]) - 97
        if memo[x] < memo[y]:
            S_new += S[i + 1]
        elif memo[x] > memo[y]:
            S_new += S[i]
        else:
            if x <= y:
                S_new += S[i]
            else:
                S_new += S[i + 1]

    memo = [0 for i in range(26)]
    for i in range(len(S_new)):
        x = ord(S_new[i]) - 97
        memo[x] += 1

    S = S_new
    print(S)
    print(memo)



print(ans)


