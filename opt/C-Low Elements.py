N = int(input())
P = list(map(int,input().split()))
ans = 0
x = P[0]


for i in P:
    if i == 1:
        ans += 1
        x = 1
    else:
        if x >= i:
            ans += 1
            x = i



            
    
print(ans)



        
