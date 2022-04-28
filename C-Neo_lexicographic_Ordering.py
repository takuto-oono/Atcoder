





def Fanction(X, s):
    t = []
    for i in range(len(s)):
        s_char = s[i]
        for j in range(len(X)):
            if X[j] == s_char:
                t.append(j)
                break

    return t


def Change_int(X, S):
    T = []
    for s in S:
        t = Fanction(X, s)
        T.append(t)

    return T

def Decryption(X, T):
    A = []
    for i in range(len(T)):
        a = ''
        for t in T[i]:
            a += X[t]
        A.append(a)

    return A

def Print_ans(A):
    for a in A:
        print(a)

def main():
    X = list(input())
    n = int(input())
    S = []
    for i in range(n):
        s = input()
        S.append(s)

    T = Change_int(X, S)
    T.sort()

    A = Decryption(X, T)

    Print_ans(A)



main()





