





def Create_string(S, T):
    ans = ''
    for t in T:
        ans += S[int(t) - 1]

    return ans

def main():
    S = []
    for i in range(3):
        s = input()
        S.append(s)

    T = input()
    print(Create_string(S, T))

main()
