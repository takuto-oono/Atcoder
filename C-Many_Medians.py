n = int(input())
X = list(map(int, input().split()))
Y = sorted(X)
condidate_min = Y[n // 2 - 1]
condidate_max = Y[n // 2]
for i in range(n):
    if X[i] <= condidate_min:
        print(condidate_max)
    else:
        print(condidate_min)


