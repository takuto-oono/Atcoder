n = int(input())
A = list(map(int, input().split()))
condidates = []
A = sorted(A)

i = 0
while(i < n - 1):
    if A[i] == A[i + 1]:
        condidates.append(A[i])
        i += 2
    else:
        i += 1

n = len(condidates)
if n >= 2:
    ans = condidates[-1] * condidates[-2]
else:
    ans = 0

print(ans)


