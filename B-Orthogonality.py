N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

inner_product = 0
for i in range(N):
    inner_product += A[i] * B[i]

if inner_product == 0:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
