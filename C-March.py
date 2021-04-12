
def main():
    n = int(input())

    First = [0 for i in range(5)]
    for i in range(n):
        s = input()
        x = s[0]
        if x == 'M':
            First[0] += 1
        elif x == 'A':
            First[1] += 1
        elif x == 'R':
            First[2] += 1
        elif x == 'C':
            First[3] += 1
        elif x == 'H':
            First[4] += 1

    ans = 0


    n = 5
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                ans += First[i] * First[j] * First[k]


    print(ans)


main()


