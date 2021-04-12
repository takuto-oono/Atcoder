O = input()
E = input()
ans = ''
for i in range(len(E)):
    ans += O[i] + E[i]

if len(E) != len(O):
    ans += O[-1]

print(ans)

