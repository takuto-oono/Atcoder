a, b = map(int,input().split())
x = []

x.append(a * b)
x.append(a - b)
x.append(a + b)

x = sorted(x)

print(x[2])
