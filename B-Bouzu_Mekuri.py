
def main():
    n = int(input())
    S = input()

    c = 0
    for i in range(n):
        if S[i] == '1':
            break
        c += 1

    if c % 2 == 0:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'

    print(ans)


main()








