N = int(input())
s = input()
t = input()
x = 0
for i in range(N):
    if i == N - 1:
        if s[-i - 1] == t[i]:
            x = 0
    elif s[-i - 1] == t[i]:
        x += 1
    else:
        break

if s == t:
    x = N

ans = 2 * N - x
print(ans)