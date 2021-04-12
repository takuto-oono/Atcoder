n = int(input())
P = list(map(int,input().split()))
l = sum(P)

def f(n, i, P):
    if n == 0:
        if i == 0:
            return True
        else:
            return False
    
    if f(n - 1, i, P):
        return True
    
    if f(n - 1, i - P[n - 1], P):
        return True
    

    return False
ans = 0
for i in range(l + 1):
    if f(n, i, P):
        ans += 1

print(ans)

