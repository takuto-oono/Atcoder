A, B = map(int,input().split())
x = 0
y = 0
z = 0

for i in range(B):
    x += A * 10 ** i

for i in range(A):
    y += B * 10 ** i

for i in range(min(A,B)):
    if x[i] < y[i]:
        print(x)
        break
    elif x[i] > y[i]:
        print(y)
        break
    else:
        z += 1

if z == B:
    print(x)
elif z == A:
    print(y)
