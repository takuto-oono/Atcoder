n, k = map(int, input().split())
r, s, p = map(int,input().split())
T = input()
S = []
for i in range(n):
    if T[i] == 'r':
        S.append(p)
    elif T[i] == 's':
        S.append(r)
    else:
        S.append(s)

Memo = [0 for i in range(n)]
ans = 0
for i in range(n):
    if i - k >= 0:
        if S[i] != S[i - k] or Memo[i - k] == 0:
            ans += S[i]
            Memo[i] = 1
        
            
    else:
        ans += S[i]
        Memo[i] = 1
    
print(ans)
