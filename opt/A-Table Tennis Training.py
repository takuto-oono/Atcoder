N, A, B = map(int,input().split())

if abs(A - B) % 2 == 0:
    ans = abs(A - B) // 2
else:
    x = max(A, B) - 1
    y = N - min(A, B)
    if x <= y:
        ans = x
    else:
        ans = y
print(ans)
