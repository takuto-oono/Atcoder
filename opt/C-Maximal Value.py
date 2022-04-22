N = int(input())
B = list(map(int,input().split()))
a = [0] * N
ans = 0
x = 0
if N == 2:
    ans = B[0] * 2
elif N == 3:
    ans = sum(B) + min(B)
else:
    for i in range(N - 1):
        if i == 0:
            a[0] = B[0]
            
        
        else:
            x = min(B[i],B[i - 1])
            a[i] = x
            
            if i == N - 2:
                a[i + 1] = B[N - 2]
                
        
        ans = sum(a)
print(ans)