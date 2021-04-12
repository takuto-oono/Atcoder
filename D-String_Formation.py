from collections import deque

S = input()
S = deque(S)
q = int(input())
j = 0
for i in range(q):
    Q = list(input().split())
    if Q[0] == '1':
        j += 1
    else:
        if (int(Q[1]) + j) % 2 == 0:
            S.append(Q[2])

        else:
            S.appendleft(Q[2])

ans = S
ans = list(ans)
if j % 2 == 1:
    ans = ans[::-1]


ans = ''.join(ans)
print(ans)











