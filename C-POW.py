a, b, c = map(int, input().split())
ans = ''

if a >= 0 and b >= 0:
    if a > b:
        ans = '>'
    elif a < b :
        ans = '<'
    else:
        ans = '='
else:
    if c % 2 == 0:
        a *= a
        b *= b
        if a > b:
            ans = '>'
        elif a < b:
            ans = '<'
        else:
            ans = '='
    else:
        if a > b:
            ans = '>'
        elif a < b:
            ans = '<'
        else:
            ans = '='

print(ans)


