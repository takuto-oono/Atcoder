S = input()
l = len(S)
ans = 1
for i in range(l + 1):
    T = S[0:l - i - 1]
    n = len(T)
    if n % 2 == 0:
        co = 0
        for i in range(n // 2):
            if T[i] == T[i + n // 2]:
                co += 2

        if co == n:
            print(co)
            exit()


