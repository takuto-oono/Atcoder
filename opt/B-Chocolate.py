N = int(input())
D, X = map(int,input().split())
ans = X
for i in range(N):
    a = 1
    A = int(input())
    while a <= D:
        a += A
        ans += 1 
print(ans)
