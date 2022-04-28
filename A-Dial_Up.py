





def Number_of_change(T):
    c = 0
    for i in range(len(T) - 1):
        if T[i] != T[i + 1]:
            c += 1

    return c

def Find_different_number(S):
    first = S[0]
    c1 = 0
    c2 = 0

    for i in range(len(S)):
        if S[i] != first:
            c1 = i
            break

    for i in range(1, len(S)):
        if S[-i] != first:
            c2 = i
            break

    c = min(c1, c2)
    return c

def main():
    n, m = map(int, input().split())
    S = list(map(int,input().split()))
    T = list(map(int, input().split()))
    ans = m
    number_of_change = Number_of_change(T)
    index_different_number = Find_different_number(S)

    if number_of_change == 0:
        if T[0] not in S:
            ans = -1

    else:
        if index_different_number == 0:
            ans = -1

        elif index_different_number == 1:
            ans += number_of_change

        else:
            ans += index_different_number + number_of_change - 1

    print(ans)



main()


