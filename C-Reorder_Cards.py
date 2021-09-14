





def Coordinate_compression(L):
    L_sorted = list(set(L))
    L_sorted = sorted(L_sorted)

    D = {v: i for i, v in enumerate(L_sorted, 1)}

    return list(map(lambda v: D[v], L))

def print_ans(A, B):
    for i in range(min(len(A), len(B))):
        a = str(A[i])
        b = str(B[i])
        ans = a + ' ' + b
        print(ans)



def main():
    h, w, n = map(int, input().split())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A = Coordinate_compression(A)
    B = Coordinate_compression(B)

    print_ans(A, B)

main()

