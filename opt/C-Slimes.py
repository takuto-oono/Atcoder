N = int(input())
S = input()
A = []
x = 0

for i in range(N):
    A.append(S[i])

for i in range(N):
    if i != N - 1:
        if A[i + 1] == A[i]:
            x += 1

print(len(A) - x)
