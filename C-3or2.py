N = int(input())
a = list(map(int,input().split()))
z = 0
ans = 0


for i in a:
    while z == 0:
        if i % 2 == 0:
            i = i // 2
            ans += 1
        else:
            z += 1
    z = 0

print(ans)
        

