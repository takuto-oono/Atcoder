





def jugemnet(S, T):
    memo = [0 for _ in range(len(T))]

    for i in range(len(S)):
        s = S[i]
        n = 0
        for j in range(len(T)):
            n = j
            if s == T[j]:
                break

        if n == 0:
            memo[0] += 1

        else:
            memo[j] += memo[j - 1]


    return memo[-1] % (10 ** 9 + 7)


def main():
    S = list(input())
    T = ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']
    S = [i for i in S if i in T]

    print(jugemnet(S, T))


main()
