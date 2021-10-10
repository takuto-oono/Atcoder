N, A, B = map(int,input().split())
ans = 0
s_1 = A * (N - 1) + B
s_2 = A + (N - 1) * B

if N != 1:
    if A <= B:
        ans = s_2 - s_1 + 1
    
else:
    if A == B:
        ans = 1

print(ans)
