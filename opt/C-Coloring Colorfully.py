S = input()
N = len(S)
a = 0
b = 0
ans = 0
for i in range(0,N,2):
    if S[i] == '0':
        a += 1
    else:
        b += 1
for i in range(1,N,2):
    if S[i] == '1':
        a += 1
    else:
        b += 1
c = max(a,b)
if c == a:
    for i in range(0,N,2):
        if S[i] != '0':
            ans += 1
    for i in range(1,N,2):
        if S[i] != '1':
            ans += 1
else:
    for i in range(0,N,2):
        if S[i] == '0':
            ans += 1
    for i in range(1,N,2):
        if S[i] == '1':
            ans += 1
print(ans)


