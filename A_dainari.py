S = input()
x = 0
nu = [0]
for i in range(len(S)):
    if S[i] == '<':
        x += 1
    else:
        x -= 1
    nu.append(x)
print(nu)
print(sum(nu))
print(len(nu))
nu = sorted(nu)
ans = sum(nu)

if nu[0] == 0:
    print(ans)
elif nu[0] > 0:
    ans -= nu[0] * len(nu)
    print(ans)
else:
    ans += abs(nu[0]) * len(nu)
    print(ans)

print(nu)
