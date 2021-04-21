S = input()
S = list(S)
ans = 0
memo = '0'
for i in range(len(S)):
    if i == 0:
        memo = S[i]
    else:
        if S[i] == memo:
            continue
        else:
            ans += 1
            memo = S[i]

print(ans)
