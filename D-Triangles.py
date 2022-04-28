n = int(input())
L = list(map(int, input().split()))
ans = 0
L = sorted(L)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if L[j + 1] >= L[j] + L[i]:
            ans += 0
        elif L[n - 1] < L[j] + L[i]:
            ans += n - j - 1
        else:
            k = j + 1
            while(k < n):
                if L[k] < L[i] + L[j]:
                    k += 1

                else:
                    break
            ans += k - (j + 1)

print(ans)
