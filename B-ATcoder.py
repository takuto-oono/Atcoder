S = input()
N = len(S)
ans = [0]
x = 0

for i in range(N):
    s = S[i]
    if s == 'A' or s == 'C' or s == 'G' or s == 'T':
        x += 1
        if i == N -1:
            ans.append(x)
    
    else:
        if x != 0:
            ans.append(x)
        x = 0
    
print(max(ans))
    