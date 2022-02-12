





def juge(L):
    if L[0] == L[1] == L[2] == L[3]:
        return 'Weak'
    else:
        if (L[1] == L[0] + 1 or (L[1] == 0 and L[0] == 9)) and (L[2] == L[1] + 1 or (L[2] == 0 and L[1] == 9)) and (L[3] == L[2] + 1 or (L[3] == 0 and L[2] == 9)):
            return 'Weak'

    return 'Strong'

def main():
    X = list(input())
    for i in range(4):
        X[i] = int(X[i])

    print(juge(X))

main()

