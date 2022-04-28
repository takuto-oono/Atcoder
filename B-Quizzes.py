N, X = map(int,input().split())
S = input()

ans = X

for i in range(N):
    if ans == 0:
        if S[i] == 'o':
            ans += 1
    else:
        if S[i] == 'o':
            ans += 1
        else:
            ans -= 1

print(ans)
