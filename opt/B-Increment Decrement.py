N = int(input())
S = input()
x = 0
a = []
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    a.append(x)
a.append(0)
a = sorted(a)
ans = a[N]
print(ans)