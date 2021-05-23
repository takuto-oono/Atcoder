S = input()
n = len(S)
ans = ''
for i in range(n):
    x = n - 1 - i
    s = S[x]
    if s == '0':
        ans += '0'
    elif s == '1':
        ans += '1'
    elif s == '6':
        ans += '9'
    elif s == '9':
        ans += '6'
    elif s == '8':
        ans += '8'

print(ans)
