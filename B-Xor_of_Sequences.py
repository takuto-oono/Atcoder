n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Ans = []

Ans = [(A[i]) for i in range(n) if A[i] not in B] + [(B[i]) for i in range(m) if B[i] not in A]
Ans = sorted((Ans))
for i in range(len(Ans)):
    Ans[i] = str(Ans[i])
ans = ' '.join(Ans)
print(ans)
