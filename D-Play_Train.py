

front_list = []
back_list = []
ans_list = []


def process_query_1(x, y):
    front_list[y - 1] = x
    back_list[x - 1] = y


def process_query_2(x, y):
    front_list[y - 1] = 0
    back_list[x - 1] = 0


def process_query_3(x):
    lead = x
    while(front_list[lead - 1] != 0):
        lead = front_list[lead - 1]

    query_ans_list = []
    while(back_list[lead - 1] != 0):
        query_ans_list.append(lead)
        lead = back_list[lead - 1]

    query_ans_list.append(lead)

    ans_list.append([len(query_ans_list)] + query_ans_list)


def print_ans_list():
    for ans in ans_list:
        print(*ans)


if __name__ == '__main__':
    n, q = map(int, input().split())
    front_list = [0 for _ in range(n)]
    back_list = [0 for _ in range(n)]

    for _ in range(q):
        query_list = list(map(int, input().split()))
        mode = query_list[0]
        if mode == 1:
            process_query_1(query_list[1], query_list[2])

        if mode == 2:
            process_query_2(query_list[1], query_list[2])

        if mode == 3:
            process_query_3(query_list[1])

    print_ans_list()
