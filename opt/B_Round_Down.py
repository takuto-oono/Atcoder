x = input()
ans = ''
l = len(x)
for i in range(l):
    if x[i] == '.':
        print(ans)
        exit()
    else:
        ans += x[i]
print(ans)