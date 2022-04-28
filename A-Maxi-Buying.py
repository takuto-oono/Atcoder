n = int(input())
n *= 1.08
n = int(n)
c = 206
ans = ''
if n == c:
    ans = 'so-so'
elif n < c:
    ans = 'Yay!'
else:
    ans = ':('
print(ans)
