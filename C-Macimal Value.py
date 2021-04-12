N = int(input())
B = list(map(int,input().split()))
a = []
m = 0
if N == 2:
    print(B[0] * 2)
elif N == 3:
    print(B[0] + B[1] + min(B[0],B[1]))
else:

    for i in range(N - 1):
        if i == 0:
            a.append(B[i])
        elif i == N - 2:
            a.append(max(a[i - 1],B[i]))
        else:
            if max(B[i],B[i - 1]) <= B[i + 1]:
                a.append(B[i])
            else:
                a.append(B[i + 1])
    

for i in range(len(a)):
    m += a[i]
print(m)
