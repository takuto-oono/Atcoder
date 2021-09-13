





def Enumeration_h(L):
    number_of_emptiness = 0
    for i in range(len(L)):
        if i == 0:
            number_of_emptiness = L[i][0] - 1
        else:
            number_of_emptiness += L[i][0] - L[i - 1][0] - 1

        L[i].append(number_of_emptiness)

    return L

def print_ans(A, B):
    A = sorted(A, reverse=False, key = lambda x: x[1])
    B = sorted(B, reverse=False, key = lambda x: x[1])
    print(A)
    print(B)
    for i in range(min(len(A), len(B))):
        a = A[i][0] - A[i][2]
        b = B[i][0] - B[i][2]
        print(str(a) + ' ' + str(b))

def main():
    h, w, n = map(int, input().split())
    A = []
    B = []

    for i in range(n):
        a, b = map(int, input().split())
        A.append([a, i])
        B.append([b, i])

    A.sort()
    B.sort()

    A = Enumeration_h(A)
    B = Enumeration_h(B)
    print_ans(A, B)

main()





