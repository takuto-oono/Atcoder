n = int(input())
H = list(map(int,input().split()))
C = [0 for i in range(n)]
ans = 0
x = 0

for i in range(n):
    if H[i] != 0:
        while(H[i] > 0):
            H[i] -= 1
            ans += 1
            for j in range(i + 1, n):
                if H[j] >= 1:
                    H[j] -= 1
                else:
                    break
    elif i == n - 1:
        ans += H[i]
    
    

print(ans)