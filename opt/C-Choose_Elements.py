def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a, b = a_list[0], b_list[0]
    for i in range(1, n):
        if a == 0 and b == 0:
            break
        aa_dif = abs(a - a_list[i])
        bb_dif = abs(b - b_list[i])
        ab_dif = abs(a - b_list[i])
        ba_dif = abs(b - a_list[i])

        if a != 0 and b != 0:
            if min(aa_dif, ba_dif) <= k:
                a = a_list[i]
            else:
                a = 0

            if min(bb_dif, ab_dif) <= k:
                b = b_list[i]
            else:
                b = 0

        elif b == 0:
            if aa_dif <= k:
                a = a_list[i]
            else:
                a = 0

            if ab_dif <= k:
                b = b_list[i]
            else:
                b = 0

        else:
            if bb_dif <= k:
                b = b_list[i]
            else:
                b = 0

            if ba_dif <= k:
                a = a_list[i]
            else:
                a = 0

    if max(a, b) > 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
