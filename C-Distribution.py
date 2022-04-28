





def transform_list(T, T_min):
    memo = 0
    A = []
    for i in range(len(T)):
        if memo == 1 or T_min == T[i][0]:
            A.append(T[i])
            memo = 1

    for i in range(len(T) - len(A)):
        A.append(T[i])

    return A

def jugement(A, S):
    for i in range(len(A)):
        if i == 0:
            continue
        else:
            id_person = A[i][1]
            get_previous_person = A[i - 1][0] + S[id_person - 1][0]
            time_min = min(A[i][0], get_previous_person)
            A[i][0] = time_min

    return A

def transform_ans(A):
    A = sorted(A, reverse=False, key=lambda x: x[1])
    return A

def main():
    n = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    T_min = min(T)

    memo = 0
    for i in range(n):
        S[i] = [S[i], i]
        T[i] = [T[i], i]

    A = transform_list(T, T_min)

    A = jugement(A, S)

    A = transform_ans(A)

    for i in range(len(A)):
        print(A[i][0])

main()




