N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N):
    B.append(float(1 / A[i]))

C = float(sum(B))

print(float(1 / C))