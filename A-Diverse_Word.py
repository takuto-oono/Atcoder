S = input()
ans = 0
n = len(S)
Co = [0 for i in range(26)]
for i in range(n):
    c = ord(S[i]) - 97
    Co[c] += 1

if 0 in Co:

    for i in range(26):
        if Co[i] == 0:
            ans = S + chr(i + 97)
            break

else:
    if S == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
        exit()
    i = 1
    memo = ord(S[n - 1])
    while(n - 1 - i >= 0):
        x = n - 1 - i
        if ord(S[x]) < memo:
            break
        else:
            memo = ord(S[x])
        i += 1

    ans = S[0:n - i - 1] + S[n - 1]
print(ans)


