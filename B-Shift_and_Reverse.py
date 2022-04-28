

if __name__ == '__main__':
    n = int(input())
    p_list = list(map(int, input().split()))

    index_1 = p_list.index(1)
    index_2 = p_list.index(2)

    if (index_1 + 1) % n == index_2:
        ans = min(index_1, p_list[::-1].index(1) + 3)

    else:
        ans = min(index_1 + 1, p_list[::-1].index(1)) + 1

    print(ans)
