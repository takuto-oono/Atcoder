l = int(input())
ans = 1
for i in range(11):
    ans *= (l - 1 - i)
    ans /= (i + 1)
    print(ans)
print(ans)