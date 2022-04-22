Q, H, S, D = map(int,input().split())
N = int(input())

q, h, s, d = 8 * Q, 4 * H, 2 * S, D
P = [q, h, s, d]
P = sorted(P)

ans = 0
for i in P:
    if i == d:
        if N // 2 > 0:
            x = N // 2
            ans += x * D
            N -= 2 * x
            
            x = 0
            
    if i == s:
        if N // 1 > 0:
            x = N // 1
            ans += x * S
            N -= x
            
            x = 0
            
    if i == h:
        if N // 0.5 > 0:
            
            x = N // 0.5
            ans += x * H
            N -=  0.5 * x
            
            x = 0
            
    if i == q:
        if N // 0.25 > 0:
            x = N // 0.25
            
            ans += x * Q
            N -= 0.25 *  x
            
            x = 0
            
ans = int(ans)
print(ans)
