import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
z = []
x = []
y = [A, B, C, D, E]
for i in range(5):
    a = math.ceil(y[i] / 10)
    a *= 10
    x.append(a)
for i in range(5):
    c = x[i] - y[i]
    z.append(c)
k = max(z)
print(sum(x) - k)

