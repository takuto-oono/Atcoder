A = int(input())
B = int(input())
C = int(input())
X = int(input())
x = 0
ans = 0
y = 0
a = [i for i in range((A + 1)* (B + 1) * (C + 1))]
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            x = 500 * i + 100 * j + 50 * k
            a[y] = x
            y += 1
ans = a.count(X)
print(ans)




