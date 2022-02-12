





def Recurrence_formula(Count_list, a):
    (Count_list[3], Count_list[4]) = (Count_list[3] + Count_list[4] + a * Count_list[2] ,Count_list[3] - a * Count_list[0])
    (Count_list[0], Count_list[1], Count_list[2]) = (Count_list[2], Count_list[0], Count_list[2] + Count_list[0])

    return Count_list


def main():
    n = int(input())
    A = list(map(int, input().split()))
    Count_list = [1, 0, 1, A[0], 0]
    for i in range(1, n):
        Count_list = Recurrence_formula(Count_list, A[i])

    ans = Count_list[4] + Count_list[3]
    print(ans % (10 ** 9 + 7))

main()


