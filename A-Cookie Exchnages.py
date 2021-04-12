A, B, C = map(int,input().split())
ans = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    a = B // 2 + C // 2
    b = A // 2 + C // 2
    c = A // 2 + B // 2
    if A == a and B == b and C == c:
        ans = -1
        break
    A = a
    B = b
    C = c
    ans += 1
print(ans)