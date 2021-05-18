import math

S = input()
S = list(S)
def permutations (n, r):
    if n < r:
        return 0
    else:
        return math.factorial(n) // math.factorial(n - r) // math.factorial(r)



co_o = 0
co_h = 0
O = []
H = []
for i in range(10):
    if S[i] == 'o':
        O.append(i)
    elif S[i] == '?':
        H.append(i)
co_o = len(O)
co_h = len(H)
ans = 0
if co_o == 0:
    ans += co_h ** 4
elif co_o == 4:
    ans = 4 * 2 * 3
elif co_o == 3:
    ans += 4 * 3 * 2 * 3 / 2
    ans += 3 * 2 * 4 * co_h
elif co_o == 2:
    ans += 2 ** 4 - 2
    ans += permutations(co_h, 2) * 24 + co_h * 24 / 2
    ans += 2 * 6 // 2 * 4 * co_h
elif co_o == 1:
    ans += 1
    ans += (permutations(co_h, 3) * 24) + (permutations(co_h, 2) * 24) + co_h * 24 / 6
    ans += (permutations(co_h, 2) * 24 / 2) + co_h * 24 / 2 / 2
    ans += co_h * 4


print(int(ans))

