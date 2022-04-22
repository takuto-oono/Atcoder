





def main():
    S = input()
    t = 'ZONe'
    ans = 0
    for i in range(len(S) - 3):
        s = S[i: i + 4]
        if s == t:
            ans += 1

    print(ans)


main()
