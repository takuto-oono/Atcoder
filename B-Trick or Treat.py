N, K = map(int,input().split())
a = []
n = 1

while n <= N:
     a = a + [n]
     n += 1
for i in range(K):
     d = int(input())
     A = list(map(int,input().split()))
     for j in range(d):
          if A[j] in a:
               a.remove(A[j])
ans = len(a)
print(ans)


