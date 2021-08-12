
def main():
    n, k = map(int, input().split())
    C = list(map(int, input().split()))

    M = {}
    for i in range(n):
        M.setdefault(C[i], 0)

    x = 0

    for i in range(k):
        if M[C[i]] == 0:
            M[C[i]] += 1
            x += 1
        else:
            M[C[i]] += 1

    ans = x

    for i in range(n - k):

        if M[C[i + k]] == 0:
            x += 1
        M[C[i + k]] += 1

        if M[C[i]] == 1:
            x -= 1
        M[C[i]] -= 1

        ans = max(ans, x)

    print(ans)






main()








