S = input()
T = input()
S = list(S)
T = list(T)

s = []
t = []
for i in range(len(S)):
    x = ord(S[i])
    s.append(x)

for i in range(len(T)):
    x = ord(T[i])
    t.append(x)

s = sorted(s)
t = sorted(t)
t = reversed(t)
x = 0
N = min(len(S), len(T))
for i in range(N):
    if int(s[i]) > int(t[i]):
        print('No')
        exit()
    elif int(s[i]) == int(t[i]):
        x += 1

if x == N:
    if len(S) >= len(T):
        print('No')
        exit()

print('Yes')




