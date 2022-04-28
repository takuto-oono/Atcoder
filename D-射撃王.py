n = int(input())
H = []
V = []
for i in range(n):
    h, v = map(int, input().split())
    H.append(h)
    V.append(v)

left = 0
right = 10 ** 18
while(right - left > 1):
    ok = True
    mid = (right + left) // 2
    T = [0 for i in range(n)]
    for i in range(n):
        if H[i] > mid:
            ok = False
            break
        else:
            T[i] = (mid - H[i]) // V[i]

    T = sorted(T)

    for i in range(n):
        if T[i] < i:
            ok = False
            break

    if ok:
        right = mid
    else:
        left = mid


print(right)

