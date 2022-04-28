





def main():
    M = ['ABC', 'ARC', 'AGC', 'AHC']
    S = []
    for i in range(3):
        s = input()
        S.append(s)

    for i in range(4):
        if M[i] not in S:
            print(M[i])
            break

main()
