n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

memo_A = 0
memo_B = 0

for i in range(n):
    memo_A = max(memo_A, A[i])
    memo_B = max(memo_B, memo_A * B[i])
    print(memo_B)



