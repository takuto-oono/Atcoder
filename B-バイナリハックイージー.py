S = input()
l = len(S)
ans = []
L = 0
for i in range(l):
    if S[i] == '0':
        ans.append('0')
        L += 1
    elif S[i] == '1':
        ans.append('1')
        L += 1
    else:
        if L != 0:
            ans.pop(-1)
            L -= 1
ans = ''.join(ans)
print(ans)
