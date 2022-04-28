n = int(input())
A = list(map(int,input().split()))
ans = 0
B = []
for i in range(n):
    b = [i + 1, A[i]]
    b = sorted(b)
    B.append(b)


ans = len(B)
B = list(map(list, set(map(tuple, B))))
ans -= len(B)
print(ans)
