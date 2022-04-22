n = int(input())
len_min = 100
C = [[0 for j in range(26)] for i in range(n)]

for i in range(n):
    S = input()
    for j in range(len(S)):
        x = ord(S[j])
        C[i][x - 97] += 1

ans = ''
y = 60
for j in range(26):
    for i in range(n):
        y = min(C[i][j], y)
    ans += chr(j + 97) * y
    y = 60

print(ans)

    


    

