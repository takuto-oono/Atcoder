n = int(input())
S = input()
Check_alu = []
Check = []

for i in range(n - 1):
    x = -1
    s = S[i]
    if s not in Check_alu:
        for j in range(i + 1, n):
            if S[j] == s:
                x = j
        
        if x != -1:
            Check.append([i, x])
            Check_alu.append(s)
l = len(Check)
ans = 0
for i in range(n):
    co = 0
    for j in range(l):
        if Check[j][0] <= i and Check[j][1] > i:
            co += 1
    ans = max(ans, co)

print(ans)

