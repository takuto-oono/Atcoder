N, M = map(int,input().split())
ans = 0
for i in range(N):
    for j in range(M):
        x = 0
        if i == 0:
            x += 1
        if i == 0 and j == 0:
            x += 1
        if i == N - 1:
            x += 1
        if j == 0:
            x += 1
        if j == M - 1:
            x += 1
        if i == 0 and j == M - 1:
            x += 1
        if i == N - 1 and j == 0:
            x += 1
        if i == N - 1 and j == M - 1:
            x += 1

        
        if x == 0:
            ans += 1
        if x == 2:
            ans += 1
        if x == 4:
            ans += 1
        if x == 6:
            ans += 1
        if  x == 8:
            ans += 1
        
        
print(ans)


            
