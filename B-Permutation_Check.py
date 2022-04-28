n = int(input())
A = list(map(int, input().split()))
B = sorted(A)
C = [i + 1 for i in range(n)]

if B == C:
    print('Yes')
else:
    print('No')
