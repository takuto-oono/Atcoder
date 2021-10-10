n = int(input())
D = []
R = []
G = []
B = []
for i in range(2 * n):
    a, c = input().split()
    D.append([a, c])
    if c == 'R':
        R.append(int(a))
    elif c == 'G':
        G.append(int(a))
    else:
        B.append(int(a))
rn = len(R)
gn = len(G)
bn = len(B)

if rn % 2 == 0 and gn % 2 == 0 and bn % 2 == 0:
    print(0)
    exit()

R = sorted(R)
G = sorted(G)
B = sorted(B)

def check(A, B):
    ans = 10 ** 16
    na = len(A)
    nb = len(B)
    j = 0
    if na >= nb:
        for i in range(nb):
            while(j < na):
                if B[i] > A[j]:
                    ans = min(B[i] - A[j], ans)
                    j += 1
                elif B[i] < A[j]:
                    ans = min(A[j] - B[i], ans)
                    break
                else:
                    return 0
        return ans
    else:
        for i in range(na):
            while(j < nb):
                if A[i] > B[j]:
                    ans = min(A[i] - B[j], ans)
                    j += 1
                elif A[i] < B[j]:
                    ans = min(B[j] - A[i], ans)
                    break
                else:
                    return 0
        return ans

if gn % 2 == 0:
    x = check(R, B)
    if x == 0:
        print(0)
    else:
        y = check(G, B) + check(G, R)
        print(min(x, y))

elif rn % 2 == 0:
    x = check(B, G)
    if x == 0:
        print(0)
    else:
        y = check(B, R) + check(G, R)
        print(min(x, y))

else:
    x = check(R, G)
    if x == 0:
        print(0)
    else:
        y = check(R, B) + check(G, B)
        print(min(x, y))


