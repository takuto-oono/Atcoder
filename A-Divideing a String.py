S = input()
ans = 0
x = ''
y = ''
for i in S:
    x += i
    if x == y:
        pass
    else:
        ans += 1
        y = x
        x = ''

print(ans)