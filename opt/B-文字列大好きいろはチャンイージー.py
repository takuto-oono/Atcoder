N, L = map(int,input().split())
A = []
for i in range(N):
    S = input()
    A.append(S)
    
A = sorted(A)
ans = ''
for i in A:
    ans += i

print(ans)
