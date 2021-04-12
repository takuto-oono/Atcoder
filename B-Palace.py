N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))
a = []
for i in H:
    t = T - i * 0.006
    a.append(t)
for i in range(N):
    a[i] = abs(a[i]- A)
x = a[0]
for i in range(N - 1):
    if x > min(a[i],a[i +  1]):
        x = min(a[i],a[i +  1])
ans = a.index(x) + 1
print(ans)

    
    