N = int(input())
S = []
for i in range(N):
    s = int(input())
    S.append(s)

ans = sum(S)
S = sorted(S)
x = 0
while x < N:
    if ans % 10 != 0:
        print(ans)
        exit()
    else:
        if S[x] % 10 != 0:
            ans -= S[x]

    x += 1

print(0)