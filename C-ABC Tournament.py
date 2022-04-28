n = int(input())
A = list(map(int,input().split()))

A_left = []
A_right = []
for i in range(n ** 2):
    if i < (n ** 2) // 2:
        A_left.append(A[i])
    else:
        A_right.append(A[i])



A_left_max = max(A_left)
A_right_max = max(A_right)

print(A.index(min(A_left_max, A_right_max)) + 1)