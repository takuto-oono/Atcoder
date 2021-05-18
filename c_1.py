S = input()
S = list(S)
import math

o = 0
h = 0

for i in range(10):
    if S[i] == 'o':
        o += 1
    elif S[i] == '?':
        h += 1

