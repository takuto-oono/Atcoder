S = input()
T = input()
x = 0
for i in range(len(S)):
    if S[i] != T[i]:
        x += 1
print(x)