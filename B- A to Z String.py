S = input()
N = len(S)
ans = 0
f = 0
b = 0

for i in range(N):
    if 'A' == S[i]:
        break
    else:
        f += 1
for i in range(1,N + 1):
    if 'Z' == S[-i]:
        break
    else:
        b += 1
b = N - b

ans = b - f
print(ans)