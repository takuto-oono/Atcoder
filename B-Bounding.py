N, X = map(int,input().split())
L = list(map(int,input().split()))
b = 0
ans = 1
for i in L:
    b += i
    if X < b:
        print(ans)
        exit()
    ans += 1


print(ans)
