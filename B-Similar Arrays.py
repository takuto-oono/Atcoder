N = int(input())
A = list(map(int,input().split()))
x = 1

for i in A:
    if i % 2 == 0:
        x *= 2
    else:
        x *= 1
    









ans = 3 ** N - x
print(ans)