S = input()
x = 0
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        x += 1
if x == 0:
    print('Good')
else:
    print('Bad')