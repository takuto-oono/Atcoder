S = input()

ans = 0
co = 0

for i in range(len(S)):
    if co == 0:
        if S[i] == 'R':
            co = 1
    else:
        if S[i] == 'R':
            co += 1
        elif S[i] == 'S':
            ans = max(co, ans)
            co = 0
    
    if i == 2:
        ans = max(co ,ans)
print(ans)

