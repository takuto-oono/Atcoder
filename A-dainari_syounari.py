S = input()
n = len(S)
A = [0 for i in range(n + 1)]

for i in range(n):
    if S[i] == '<':
        A[i + 1] = max(A[i] + 1, A[i + 1])
    

for i in range(n):
    
    if S[n - 1 - i] == '>':
        A[n - 1 - i] = max(A[n - 0 - i] + 1, A[n - 1 - i])


print(sum(A))
