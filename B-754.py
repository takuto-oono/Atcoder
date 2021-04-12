S = input()
N = len(S)
y = []
for i in range(N -2):
    X = int(S[i:i + 3])
    z = int(abs(X - 753))
    y.append(z)

y = sorted(y)
print(y[0])
    