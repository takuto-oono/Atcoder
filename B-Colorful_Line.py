query_list = []
count_by_color_list = []
h = 0
w = 0


def count_by_color() -> None:
    row_count, column_count = 0, 0
    is_used_row_dic = {}
    is_used_column_dic = {}

    for query in query_list:
        t = query[0]
        n = query[1]
        c = query[2]

        if t == 1:
            if n in is_used_row_dic:
                continue

            is_used_row_dic[n] = False

            count_by_color_list[c - 1] += w - column_count
            row_count += 1

        if t == 2:
            if n in is_used_column_dic:
                continue

            is_used_column_dic[n] = False

            count_by_color_list[c - 1] += h - row_count
            column_count += 1

    print(*count_by_color_list)


if __name__ == "__main__":
    h, w, c, q = map(int, input().split())
    count_by_color_list = [0 for _ in range(c)]
    for _ in range(q):
        t, n, c = map(int, input().split())
        query_list.append([t, n, c])

    query_list.reverse()
    count_by_color()
