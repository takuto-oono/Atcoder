S = input()

n = len(S)
ans = n * (n - 1)
x = 0

for i in range(n):
    if S[i] == 'D':
        ans += n - i - 1
    else:
        ans += i


print(ans)




