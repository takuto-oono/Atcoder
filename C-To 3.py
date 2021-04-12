N = input()
A = list(N)
for i in range(len(A)):
    A[i] = int(A[i]) % 3
x = 0
y = 0
z = 0
for i in range(len(A)):
    if A[i] == 1:
        x += 1
    elif A[i] == 2:
        y += 1
    else:
        z += 1


ans = abs(x - y) % 3
if ans >= len(A):
    ans = -1
print(ans)