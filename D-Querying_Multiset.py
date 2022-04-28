import heapq


multiset_heapq = []
ans_list = []
sum = 0


def process_1(x):
    heapq.heappush(multiset_heapq, x - sum)


def process_2(x, sum):
    return sum + x


def process_3():
    ans_list.append(heapq.heappop(multiset_heapq) + sum)


def print_ans():
    for ans in ans_list:
        print(ans)


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        mode = query[0]

        if mode == 1:
            process_1(query[1])

        if mode == 2:
            sum = process_2(query[1], sum)

        if mode == 3:
            process_3()

    print_ans()
