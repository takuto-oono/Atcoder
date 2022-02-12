S = input()
a_co = 0
b_co = 0
c_co = 0
n = len(S)

for i in S:
    if i == 'a':
        a_co += 1
    elif i == 'b':
        b_co += 1
    elif i == 'c':
        c_co += 1

x = n % 3

C = [a_co, b_co, c_co]
C = sorted(C)
if x == 0:
    if C[0] == C[2]:
        ans = 'YES'
    else:
        ans = 'NO'
elif x == 1:
    if C[2] - C[1] == 1 and C[1] - C[0] == 0:
        ans = 'YES'
    else:
        ans = 'NO'
else:
    if C[2] == C[1] and C[1] - C[0] == 1:
        ans = 'YES'
    else:
        ans = 'NO'

print(ans)

