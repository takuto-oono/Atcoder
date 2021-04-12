k, a, b = map(int,input().split())
ans = 1
if b - a <= 2:
    ans += k
else:
    if ans < a:
        if k < a:
            ans += k
        else:
            ans += a - 1
            k -= a - 1
            ans += (k // 2) * (b - a)
            if k % 2 == 1:
                ans += 1
    else:
        ans += (k // 2) * (b - a)
        if k % 2 == 1:
            ans += 1

print(ans)


        


