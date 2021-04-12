n = int(input())
S = input()
T = input()

if S == T:
    ans = n
else:
    co = 0
    for i in range(1, n):
        
        if S[n - i: n] == T[0 : i]:
            co = max(co, i)
    
    ans = 2 * n - co

print(ans)

